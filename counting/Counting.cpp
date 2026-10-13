#include <stdio.h>
#include <vector>
#include <random>
#include <chrono>
#include <exception>
#include <windows.h>
#include <psapi.h>
using namespace std;

// Ordena reales con 2 decimales entre 0.00 y 999.99 (maximo = 99999)
void countingSort(vector<double>& arr, int maximo) {
    vector<int> conteo(maximo + 1, 0);

    for (size_t i = 0; i < arr.size(); i++) {
        conteo[(int)(arr[i] * 100 + 0.5)]++;
    }

    size_t pos = 0;
    for (int v = 0; v <= maximo; v++) {
        double valor = v / 100.0;
        while (conteo[v] > 0) {
            arr[pos] = valor;
            pos++;
            conteo[v]--;
        }
    }
}

// Pico de memoria usada por el programa, en MB
double memoriaPicoMB() {
    PROCESS_MEMORY_COUNTERS pmc;
    GetProcessMemoryInfo(GetCurrentProcess(), &pmc, sizeof(pmc));
    return pmc.PeakWorkingSetSize / (1024.0 * 1024.0);
}

int main() {
    int n = 1000000000;   // aqui cambias el tamano en cada corrida

    mt19937 gen(42);
    uniform_int_distribution<int> dist(0, 99999);

    // Reservar memoria; si no se puede, avisar y terminar
    vector<double> datos;
    try {
        datos.resize(n);
    } catch (exception&) {
        printf("n = %d | No ejecutable: el arreglo necesita %.2f GB y supera el limite de memoria del programa\n",
               n, n * 8.0 / (1024.0 * 1024.0 * 1024.0));
        return 1;
    }

    // Llenar con reales de 2 decimales
    for (int i = 0; i < n; i++) {
        datos[i] = dist(gen) / 100.0;
    }

    // Medir tiempo del ordenamiento
    auto inicio = chrono::high_resolution_clock::now();
    countingSort(datos, 99999);
    auto fin = chrono::high_resolution_clock::now();
    double ms = chrono::duration<double, milli>(fin - inicio).count();

    // Comprobar que quedo ordenado
    bool ordenado = true;
    for (int i = 1; i < n; i++) {
        if (datos[i - 1] > datos[i]) { ordenado = false; break; }
    }

    printf("n = %d | Tiempo: %.3f ms | Memoria pico: %.2f MB | Ordenado: %s\n",
           n, ms, memoriaPicoMB(), ordenado ? "SI" : "NO");
    return 0;
}

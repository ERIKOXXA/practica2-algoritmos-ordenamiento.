#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <iomanip>
#include <new> // Necesario para atrapar errores de memoria (std::bad_alloc)

using namespace std;
using namespace std::chrono;

// Algoritmo Bubble Sort Clásico O(N^2)
void bubbleSort(vector<double>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        // Si no hubo intercambios, el arreglo ya está ordenado
        if (!swapped) break;
    }
}

int main() {
    // Los tamaños masivos exactos solicitados en la práctica
    vector<long long> tamanos = {100000, 1000000, 10000000, 100000000, 1000000000};
    
    cout << left << setw(15) << "N Elementos" 
         << setw(25) << "Tiempo (s)" 
         << setw(20) << "Memoria RAM (MB)" << "\n";
    cout << string(60, '-') << "\n";

    random_device rd;
    mt19937 gen(rd());
    // Generador de números reales (flotantes dobles de 8 bytes)
    uniform_real_distribution<double> dist(1.0, 1000.0);

    for (long long n : tamanos) {
        try {
            // El consumo de memoria en C++ es exacto: N elementos * 8 bytes (tamaño de un double)
            // Se asume O(1) de memoria extra por parte del Bubble Sort.
            double memoria_mb = (n * sizeof(double)) / (1024.0 * 1024.0);
            
            // Intentar reservar la memoria. Aquí es donde los tamaños grandes pondrán a prueba tu PC.
            vector<double> arr(n);
            
            // Llenar el vector con datos reales aleatorios
            for (long long i = 0; i < n; ++i) {
                arr[i] = dist(gen);
            }

            auto inicio = high_resolution_clock::now();
            
            // Ejecutar ordenamiento
            bubbleSort(arr);
            
            auto fin = high_resolution_clock::now();
            double tiempo_total = duration<double>(fin - inicio).count();

            cout << left << setw(15) << n 
                 << setw(25) << fixed << setprecision(4) << tiempo_total 
                 << setw(20) << memoria_mb << "\n";

        } catch (const std::bad_alloc& e) {
            // Si el Sistema Operativo niega la memoria (ej. al pedir 8GB de golpe), entra aquí.
            cout << left << setw(15) << n 
                 << setw(25) << "Error: Out of RAM" 
                 << setw(20) << "Supera Limite" << "\n";
        }
    }
    
    return 0;
}
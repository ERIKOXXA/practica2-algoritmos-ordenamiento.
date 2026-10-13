#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <iomanip>
#include <fstream>
#include <exception>

// 1. Algoritmo Heapsort para números reales (double)
void heapify(std::vector<double>& arr, int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;

    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(std::vector<double>& arr) {
    int n = arr.size();
    // Construir el Max-Heap
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    // Extraer elementos uno a uno
    for (int i = n - 1; i > 0; i--) {
        std::swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
    // Tamaños requeridos por la práctica (100k, 1M, 10M, 100M, 1B)
    std::vector<long long> tamanos = {100000, 1000000, 10000000, 100000000, 1000000000};
    
    std::ofstream archivo_csv("resultados_heapsort.csv");
    archivo_csv << "Tamano,Tiempo(s),Memoria(MB)\n";

    std::cout << std::left << std::setw(15) << "Tamaño (N)" 
              << std::setw(20) << "Tiempo (s)" 
              << std::setw(20) << "Memoria (MB)" << "\n";
    std::cout << std::string(55, '-') << "\n";

    std::mt19937 gen(42); // Semilla fija para reproducibilidad
    std::uniform_real_distribution<double> distrib(1.0, 10000.0); // Números reales

    for (long long size : tamanos) {
        try {
            // Generar arreglo de números reales
            std::vector<double> dataset(size);
            for (long long i = 0; i < size; ++i) {
                dataset[i] = distrib(gen);
            }

            // Cálculo de memoria consumida por el arreglo (in-place sort)
            // size * 8 bytes (tamaño de un double) pasado a Megabytes
            double memoria_mb = (double)(dataset.capacity() * sizeof(double)) / (1024.0 * 1024.0);

            // Medir el tiempo de ejecución de Heapsort
            auto inicio = std::chrono::high_resolution_clock::now();
            heapSort(dataset);
            auto fin = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> tiempo_ejecucion = fin - inicio;

            // Mostrar e imprimir en CSV
            std::cout << std::left << std::setw(15) << size 
                      << std::setw(20) << std::fixed << std::setprecision(4) << tiempo_ejecucion.count() 
                      << std::setw(20) << std::fixed << std::setprecision(2) << memoria_mb << "\n";

            archivo_csv << size << "," << std::fixed << std::setprecision(4) << tiempo_ejecucion.count() 
                        << "," << std::fixed << std::setprecision(2) << memoria_mb << "\n";
            
            // Liberar memoria explícitamente antes de la siguiente iteración gigante
            dataset.clear();
            dataset.shrink_to_fit();

        } catch (const std::bad_alloc& e) {
            std::cout << "FALLO por falta de memoria RAM al intentar crear arreglo de tamaño: " << size << "\n";
            archivo_csv << size << ",RAM_INSUFICIENTE,RAM_INSUFICIENTE\n";
            break; // Romper el ciclo si ya no hay RAM
        }
    }

    archivo_csv.close();
    std::cout << "\nPruebas finalizadas. Resultados guardados en 'resultados_heapsort.csv'." << std::endl;
    return 0;
}
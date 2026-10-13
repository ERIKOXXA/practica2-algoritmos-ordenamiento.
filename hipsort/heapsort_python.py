import random
import time
import csv
import sys

# 1. Algoritmo Heapsort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# 2. Ejecución y Medición
def ejecutar_pruebas():
    tamanos = [100000, 1000000, 10000000, 100000000, 1000000000]
    
    with open('resultados_python.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Tamano", "Tiempo(s)", "Memoria(MB)"])
        
        print(f"{'Tamaño (N)':<15} | {'Tiempo (s)':<15} | {'Memoria (MB)':<15}")
        print("-" * 50)
        
        for size in tamanos:
            try:
                # Calcular memoria en Python: 24 bytes (float) + 8 bytes (puntero en lista) = 32 bytes por elemento
                memoria_mb = (size * 32) / (1024 * 1024)
                
                # Generar arreglo
                dataset = [random.uniform(1.0, 10000.0) for _ in range(size)]
                
                # Cronometrar Heapsort
                inicio = time.perf_counter()
                heap_sort(dataset)
                fin = time.perf_counter()
                
                tiempo = fin - inicio
                print(f"{size:<15} | {tiempo:<15.4f} | {memoria_mb:<15.2f}")
                writer.writerow([size, f"{tiempo:.4f}", f"{memoria_mb:.2f}"])
                
                # Liberar memoria forzosamente antes del siguiente ciclo
                del dataset
                
            except MemoryError:
                # Este error saltará cuando Python se quede sin RAM
                print(f"FALLO por falta de memoria RAM (MemoryError) en tamaño: {size}")
                writer.writerow([size, "RAM_INSUFICIENTE", "RAM_INSUFICIENTE"])
                break

if __name__ == '__main__':
    print("Iniciando pruebas de Heapsort en Python...")
    print("ADVERTENCIA: Los tamaños de 10M y 100M tomarán bastante tiempo.")
    ejecutar_pruebas()
    print("Pruebas finalizadas. Resultados guardados en 'resultados_python.csv'")
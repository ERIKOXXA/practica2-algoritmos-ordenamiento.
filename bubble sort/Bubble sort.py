import time
import tracemalloc
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def ejecutar_pruebas():
    tamanos = [1000, 2000, 5000, 10000, 20000]
    
    print(f"{'N Elementos':<15} | {'Tiempo (s)':<20} | {'Memoria Pico (MB)':<20}")
    print("-" * 60)

    for n in tamanos:
        arr = np.random.rand(n)
        
        tracemalloc.start()
        inicio = time.perf_counter()
        
        bubble_sort(arr)
        
        fin = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        tiempo_total = fin - inicio
        memoria_mb = peak / (1024 * 1024) 
        
        print(f"{n:<15} | {tiempo_total:<20.4f} | {memoria_mb:<20.4f}")

if __name__ == "__main__":
    ejecutar_pruebas()
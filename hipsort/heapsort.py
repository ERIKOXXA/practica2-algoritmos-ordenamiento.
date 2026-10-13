import csv
import matplotlib.pyplot as plt

# 1. IMPLEMENTACIÓN EN PYTHON (Segundo Lenguaje requerido)
# Ojo: Aquí está el algoritmo escrito, pero las pruebas masivas 
# ya las hicimos en C++ porque Python no soportaría esos tamaños de memoria.

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


# 2. GENERACIÓN DE GRÁFICAS DEL REPORTE
def graficar_resultados_cxx():
    tamanos = []
    tiempos = []
    memorias = []

    # Leer los datos generados por el programa de C++
    with open('resultados_heapsort.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Tiempo(s)'] != 'RAM_INSUFICIENTE':
                tamanos.append(int(row['Tamano']))
                tiempos.append(float(row['Tiempo(s)']))
                memorias.append(float(row['Memoria(MB)']))

    # Crear el lienzo para las dos gráficas
    plt.figure(figsize=(14, 6))

    # Gráfica 1: Tiempo de Ejecución
    plt.subplot(1, 2, 1)
    plt.plot(tamanos, tiempos, marker='o', color='#e74c3c', linewidth=2)
    plt.title('Heapsort: Tiempo de Ejecución (O(n log n))')
    plt.xlabel('Tamaño del Arreglo (N)')
    plt.ylabel('Tiempo (segundos)')
    plt.xscale('log') # Escala logarítmica para ver bien las diferencias
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)

    # Gráfica 2: Consumo de Memoria
    plt.subplot(1, 2, 2)
    plt.plot(tamanos, memorias, marker='s', color='#2980b9', linewidth=2)
    plt.title('Heapsort: Consumo de Memoria RAM')
    plt.xlabel('Tamaño del Arreglo (N)')
    plt.ylabel('Memoria (Megabytes)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)

    plt.suptitle('Evaluación de Rendimiento Heapsort (C++)', fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print("Algoritmo Heapsort en Python cargado correctamente.")
    print("Generando gráficas comparativas a partir de los resultados en C++...")
    graficar_resultados_cxx()
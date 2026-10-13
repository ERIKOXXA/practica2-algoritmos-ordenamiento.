import random
import time
import sys
from array import array
import psutil


def counting_sort(arr, maximo):
    # 1. Una casilla de conteo por cada valor posible (0 hasta maximo)
    conteo = [0] * (maximo + 1)

    # 2. Contar cuantas veces aparece cada valor (el real se escala x100)
    for x in arr:
        conteo[int(x * 100 + 0.5)] += 1

    # 3. Reescribir el arreglo en orden, usando los conteos
    pos = 0
    for v in range(maximo + 1):
        c = conteo[v]
        if c > 0:
            valor = v / 100.0
            arr[pos:pos + c] = array('d', [valor]) * c
            pos += c


def memoria_pico_mb():
    # Pico de memoria del proceso (solo Windows)
    return psutil.Process().memory_info().peak_wset / (1024 * 1024)


n = 1000000000 # aqui cambias el tamano en cada corrida

random.seed(42)
try:
    datos = array('d', (random.randrange(100000) / 100.0 for _ in range(n)))
except MemoryError:
    print(f"n = {n} | No ejecutable: falta memoria para el arreglo")
    sys.exit(1)

# Medir tiempo del ordenamiento
inicio = time.perf_counter()
counting_sort(datos, 99999)
fin = time.perf_counter()
ms = (fin - inicio) * 1000

# Comprobar que quedo ordenado
ordenado = all(datos[i - 1] <= datos[i] for i in range(1, n))

print(f"n = {n} | Tiempo: {ms:.3f} ms | Memoria pico: {memoria_pico_mb():.2f} MB | Ordenado: {'SI' if ordenado else 'NO'}")
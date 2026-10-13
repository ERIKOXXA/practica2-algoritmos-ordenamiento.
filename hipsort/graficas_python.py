import csv
import matplotlib.pyplot as plt

def graficar_resultados_python():
    tamanos = []
    tiempos = []
    memorias = []

    try:
        # Asegúrate de que el nombre coincide con el archivo generado
        with open('resultados_python.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Omitir las filas donde la memoria no fue suficiente
                if row['Tiempo(s)'] != 'RAM_INSUFICIENTE':
                    tamanos.append(int(row['Tamano']))
                    tiempos.append(float(row['Tiempo(s)']))
                    memorias.append(float(row['Memoria(MB)']))
    except FileNotFoundError:
        print("Error: No se encontró 'resultados_python.csv'. Ejecuta primero las pruebas de Python.")
        return

    # Configuración del lienzo
    plt.figure(figsize=(14, 6))

    # Gráfica 1: Tiempo de Ejecución (Python)
    plt.subplot(1, 2, 1)
    plt.plot(tamanos, tiempos, marker='o', color='#8e44ad', linewidth=2)
    plt.title('Heapsort en Python: Tiempo de Ejecución')
    plt.xlabel('Tamaño del Arreglo (N)')
    plt.ylabel('Tiempo (segundos)')
    plt.xscale('log') 
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)

    # Gráfica 2: Consumo de Memoria (Python)
    plt.subplot(1, 2, 2)
    plt.plot(tamanos, memorias, marker='s', color='#f39c12', linewidth=2)
    plt.title('Heapsort en Python: Consumo de Memoria RAM')
    plt.xlabel('Tamaño del Arreglo (N)')
    plt.ylabel('Memoria (Megabytes)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)

    plt.suptitle('Evaluación de Rendimiento Heapsort (Python)', fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    graficar_resultados_python()
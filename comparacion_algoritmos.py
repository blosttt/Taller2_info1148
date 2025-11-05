import time
import random

def bubble_sort(arr):
    """
    Bubble Sort - Complejidad:
    - Peor caso: O(n²)
    - Mejor caso: O(n) (lista ordenada)
    - Caso promedio: O(n²)
    - Espacial: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(arr):
    """
    Merge Sort - Complejidad:
    - Peor caso: O(n log n)
    - Mejor caso: O(n log n)
    - Caso promedio: O(n log n)
    - Espacial: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """
    Quick Sort - Complejidad:
    - Peor caso: O(n²) (pivote mal elegido)
    - Mejor caso: O(n log n)
    - Caso promedio: O(n log n)
    - Espacial: O(log n) a O(n)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
import time
import matplotlib.pyplot as plt
import numpy as np

def medir_tiempo(algoritmo, arr):
    """Mide el tiempo de ejecución de un algoritmo"""
    start_time = time.time()
    algoritmo(arr.copy())  # Usamos copia para no modificar el original
    end_time = time.time()
    return end_time - start_time

def comparar_algoritmos():
    """Compara el rendimiento de los tres algoritmos"""
    tamanos = [100, 500, 1000, 2000, 5000]
    algoritmos = {
        'Bubble Sort': bubble_sort,
        'Merge Sort': merge_sort, 
        'Quick Sort': quick_sort
    }
    
    resultados = {nombre: [] for nombre in algoritmos}
    
    for tamano in tamanos:
        print(f"Probando con tamaño: {tamano}")
        # Generar array aleatorio
        arr = [random.randint(1, 10000) for _ in range(tamano)]
        
        for nombre, algoritmo in algoritmos.items():
            tiempo = medir_tiempo(algoritmo, arr)
            resultados[nombre].append(tiempo)
            print(f"  {nombre}: {tiempo:.4f} segundos")
    
    return tamanos, resultados

def graficar_resultados(tamanos, resultados):
    """Genera gráficos comparativos"""
    plt.figure(figsize=(12, 5))
    
    # Gráfico lineal
    plt.subplot(1, 2, 1)
    for nombre, tiempos in resultados.items():
        plt.plot(tamanos, tiempos, marker='o', label=nombre, linewidth=2)
    
    plt.xlabel('Tamaño del Array')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Tiempos de Ejecución')
    plt.legend()
    plt.grid(True)
    
    # Gráfico logarítmico para ver crecimiento asintótico
    plt.subplot(1, 2, 2)
    for nombre, tiempos in resultados.items():
        plt.plot(tamanos, tiempos, marker='o', label=nombre, linewidth=2)
    
    plt.xlabel('Tamaño del Array')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Escala Logarítmica - Crecimiento Asintótico')
    plt.legend()
    plt.yscale('log')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('comparacion_algoritmos.png', dpi=300)
    plt.show()

# Ejecutar comparación
if __name__ == "__main__":
    print("=== COMPARACIÓN DE ALGORITMOS DE ORDENAMIENTO ===")
    print("Analizando complejidad temporal...")
    
    tamanos, resultados = comparar_algoritmos()
    graficar_resultados(tamanos, resultados)
    
    print("\n=== ANÁLISIS TEÓRICO ===")
    print("Bubble Sort: O(n²) - Cuadrático")
    print("Merge Sort: O(n log n) - Linealítmico") 
    print("Quick Sort: O(n log n) promedio - Linealítmico")

def analizar_complejidad_espacial():
    """Analiza y compara la complejidad espacial"""
    complejidades = {
        'Bubble Sort': {
            'teorica': 'O(1)',
            'explicacion': 'Solo usa variables auxiliares, no requiere memoria adicional significativa'
        },
        'Merge Sort': {
            'teorica': 'O(n)',
            'explicacion': 'Requiere arrays auxiliares para el proceso de mezcla'
        },
        'Quick Sort': {
            'teorica': 'O(log n) a O(n)',
            'explicacion': 'Depende de la implementación y la elección del pivote'
        }
    }
    
    print("\n=== COMPLEJIDAD ESPACIAL ===")
    for algoritmo, info in complejidades.items():
        print(f"{algoritmo}: {info['teorica']}")
        print(f"  → {info['explicacion']}\n")
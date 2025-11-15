import time
import random
import math
import statistics
import matplotlib.pyplot as plt
import numpy as np
#importacion de codigos algoritmos (quicksort,mergesort,bubblesort)
from quicksort import quicksort
from mergesort import mergesort
from bubblesort import bubble_sort


class AlgorithmBenchmark:
    def __init__(self):
        self.algoritmos = {
            "QuickSort": {"funcion": quicksort},
            "MergeSort": {"funcion": mergesort},
            "BubbleSort": {"funcion": bubble_sort},
        }

        self.resultados = {name: [] for name in self.algoritmos}
        self.resultados_detallados = []

    def medir_tiempo(self, func, datos, rep=3):
        tiempos = []
        for _ in range(rep):
            arr = datos.copy()
            inicio = time.perf_counter()
            func(arr)
            fin = time.perf_counter()
            tiempos.append(fin - inicio)
        return statistics.mean(tiempos)

    def generar_datos(self, n, tipo):
        if tipo == "ordenado":
            return list(range(n))
        if tipo == "inverso":
            return list(range(n, 0, -1))
        if tipo == "duplicados":
            return [random.randint(1, n // 10) for _ in range(n)]
        return [random.randint(1, 100000) for _ in range(n)]

    def ejecutar(self, tamanos, tipos, rep=3):
        for tipo in tipos:
            print(f"\n============================")
            print(f"### TIPO DE DATOS: {tipo}")
            print(f"============================")

            for n in tamanos:
                datos = self.generar_datos(n, tipo)
                print(f"\n---- Tamaño n = {n} ----")

                for nombre, cfg in self.algoritmos.items():

                    if nombre == "BubbleSort" and n > 4000:
                        continue

                    t = self.medir_tiempo(cfg["funcion"], datos, rep)

                    self.resultados[nombre].append(
                        {"n": n, "tipo": tipo, "tiempo": t}
                    )

                    self.resultados_detallados.append(
                        {"algoritmo": nombre, "tamaño": n,
                         "tipo": tipo, "tiempo": t}
                    )

                    print(f"{nombre:<12} → {t*1000:.4f} ms")

    def imprimir_tablas_para_graficos(self):
        print("\n========================================")
        print(" TABLA 1: Tiempo vs n (datos aleatorios)")
        print("========================================")
        for nombre, datos in self.resultados.items():
            for d in [x for x in datos if x["tipo"] == "aleatorio"]:
                print(f"{nombre:<12} | n={d['n']:<5} | {d['tiempo']*1000:.4f} ms")

        print("\n========================================")
        print(" TABLA 2: Log-log")
        print("========================================")
        for nombre, datos in self.resultados.items():
            for d in [x for x in datos if x["tipo"] == "aleatorio"]:
                print(f"{nombre:<12} | log(n)={math.log10(d['n']):.4f} | "
                      f"log(ms)={math.log10(d['tiempo']*1000):.4f}")

        print("\n===================================================")
        print(" TABLA 3: Comparación por tipo (n máximo)")
        print("===================================================")
        tam_max = max(r["tamaño"] for r in self.resultados_detallados)
        for r in [x for x in self.resultados_detallados if x["tamaño"] == tam_max]:
            print(f"{r['algoritmo']:<12} | tipo={r['tipo']:<10} | {r['tiempo']*1000:.4f} ms")

        print("\n========================================")
        print(" TABLA 4: Speedup (VS BubbleSort)")
        print("========================================")

        datos_bubble = [d for d in self.resultados["BubbleSort"] if d["tipo"] == "aleatorio"]

        for nombre in ["QuickSort", "MergeSort"]:
            datos_algo = [d for d in self.resultados[nombre] if d["tipo"] == "aleatorio"]

            for d in datos_algo:
                b = [x for x in datos_bubble if x["n"] == d["n"]]
                if b:
                    speedup = b[0]["tiempo"] / d["tiempo"]
                    print(f"{nombre:<12} | n={d['n']:<5} | Speedup={speedup:.3f}")

    def graficar(self):

        fig = plt.figure(figsize=(16, 10))

        # grafico 1
        ax1 = plt.subplot(2, 2, 1)
        for nombre, datos in self.resultados.items():
            arr = [d for d in datos if d["tipo"] == "aleatorio"]
            if arr:
                ns = [d["n"] for d in arr]
                ts = [d["tiempo"] * 1000 for d in arr]
                ax1.plot(ns, ts, marker='o', label=nombre)

        ax1.set_title("Rendimiento - Aleatorio")
        ax1.set_xlabel("n")
        ax1.set_ylabel("Tiempo (ms)")
        ax1.grid(True)
        ax1.legend()

        # grafico 2
        ax2 = plt.subplot(2, 2, 2)
        for nombre, datos in self.resultados.items():
            arr = [d for d in datos if d["tipo"] == "aleatorio"]
            if arr:
                ns = [d["n"] for d in arr]
                ts = [d["tiempo"] * 1000 for d in arr]
                ax2.loglog(ns, ts, marker='s', label=nombre)

        ax2.set_title("Escala Logarítmica")
        ax2.set_xlabel("n (log)")
        ax2.set_ylabel("Tiempo (ms) (log)")
        ax2.grid(True)
        ax2.legend()

        # grafico 3
        ax3 = plt.subplot(2, 2, 3)
        tam_max = max(r["tamaño"] for r in self.resultados_detallados)
        tipos = sorted({r["tipo"] for r in self.resultados_detallados})
        x = np.arange(len(tipos))
        width = 0.25

        for i, nombre in enumerate(self.algoritmos):
            vals = []
            for t in tipos:
                match = [
                    r["tiempo"] * 1000
                    for r in self.resultados_detallados
                    if r["algoritmo"] == nombre and
                       r["tipo"] == t and
                       r["tamaño"] == tam_max
                ]
                vals.append(match[0] if match else 0.001)

            ax3.bar(x + i * width, vals, width, label=nombre)

        ax3.set_title(f"Comparación por Tipo (n={tam_max})")
        ax3.set_xlabel("Tipo de datos")
        ax3.set_ylabel("Tiempo (ms) [log]")
        ax3.set_yscale("log")
        ax3.grid(True, which="both", linestyle="--")
        ax3.set_xticks(x + width)
        ax3.set_xticklabels(tipos)

        # grafico 4
        ax4 = plt.subplot(2, 2, 4)
        datos_bubble = [d for d in self.resultados["BubbleSort"] if d["tipo"] == "aleatorio"]

        for nombre in ["QuickSort", "MergeSort"]:
            datos_algo = [d for d in self.resultados[nombre] if d["tipo"] == "aleatorio"]
            ns = []
            sp = []
            for d in datos_algo:
                b = [x for x in datos_bubble if x["n"] == d["n"]]
                if b:
                    ns.append(d["n"])
                    sp.append(b[0]["tiempo"] / d["tiempo"])
            if ns:
                ax4.plot(ns, sp, marker='^', label=f"{nombre} vs BubbleSort")

        ax4.set_title("Speedup vs BubbleSort")
        ax4.set_xlabel("n")
        ax4.set_ylabel("Speedup (x)")
        ax4.grid(True)
        ax4.legend()

        plt.tight_layout()
        plt.show()


def main():
    prueba = AlgorithmBenchmark()

    prueba.ejecutar(
        tamanos=[100, 500, 1000, 2000, 3000],
        tipos=["aleatorio", "ordenado", "inverso"],
        rep=3
    )

    prueba.imprimir_tablas_para_graficos()
    prueba.graficar()


if __name__ == "__main__":
    main()

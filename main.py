from benchmarking.benchmark import benchmark
from algoritmos.grasp import grasp_aleatorio
import csv
import matplotlib.pyplot as plt
import numpy as np


archivo_entrada = "benchmarking/in/data.csv"
out_folder = "benchmarking/out/"

alphas = []
for i in range(4):
    alphas.append(0.6 + i / 10)

def graficar(datos , alpha):

    iteraciones = []
    precisiones = []

    for dato in datos:
        try:
            with open(dato[0], mode='r', newline='') as file:
                rows = list(csv.reader(file))
                for row in reversed(rows):
                    if row and row[0] == "promedio_precision_porcentual":
                        promedio = float(row[1])
                        iteraciones.append(int(dato[1]))
                        precisiones.append(float(promedio))
                        print(f"{file}: {promedio:.2f}% precisión")
                        break
        except Exception as e:
            print(f"Error leyendo {file}: {e}")

    iteraciones = np.array(iteraciones)
    precisiones = np.array(precisiones)

    print(iteraciones, precisiones)
    plt.bar(iteraciones, precisiones, width=40, color='purple')
    plt.xlim(20, 1100)
    plt.ylim(min(precisiones) - 5, 100)

    plt.title("Precisión promedio de GRASP vs Iteraciones con alpha: " + str(alpha))
    plt.xlabel("Iteraciones (α)")
    plt.ylabel("Precisión promedio (%)")
    plt.xticks(iteraciones)
    plt.grid(axis='y')

    nombre_archivo = "benchmarking/out/grafico_barras_precision_alpha_" + str(alpha * 10) + ".jpg"
    plt.savefig(nombre_archivo)
    plt.close()

    print(f"✅ Gráfico guardado como: {nombre_archivo}")

iteraciones = [50, 100, 200, 400, 500, 1000]

if __name__ == "__main__":
    for alpha in alphas:
        datos = []
        for it in iteraciones:
            out_file = out_folder + "benchmark_grasp_aleatorio_" + str(alpha * 10) + "_iteraciones_" + str(it) + ".csv"
            benchmark(archivo_entrada, out_file, lambda x, y: grasp_aleatorio(x, y, 2000, alpha))
            datos.append((out_file, it))
        graficar(datos, alpha)
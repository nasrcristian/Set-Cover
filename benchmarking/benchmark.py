import csv
import ast

def benchmark(archivo_entrada: str, archivo_salida: str, algoritmo):

    resultados = []
    precisiones = []

    with open(archivo_entrada, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for fila in reader:
            try:
                optimo = int(fila["min_cant_subconjuntos"])
                U = set(ast.literal_eval(fila["conjunto_universal"]))
                subconjuntos = [set(s) for s in ast.literal_eval(fila["lista_subconjuntos"])]

                grasp_resultado = algoritmo(U, subconjuntos)[0]

                if grasp_resultado == 0:
                    precision = 0.0
                else:
                    precision = (optimo / grasp_resultado) * 100

                resultados.append((grasp_resultado, round(precision, 2)))
                precisiones.append(precision)

            except Exception as e:
                print(f"⚠️ Error procesando fila: {e}")

    promedio_precision = sum(precisiones) / len(precisiones)

    with open(archivo_salida, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["grasp_resultado", "precision_porcentual"])

        for grasp_resultado, precision in resultados:
            writer.writerow([grasp_resultado, precision])

        writer.writerow([]) 
        writer.writerow(["promedio_precision_porcentual", round(promedio_precision, 2)])

    print(f"✅ Archivo generado: {archivo_salida}")
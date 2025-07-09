import csv
import random
from algoritmos.dinamica import dinamica_bottom_up

# Esta es una función dummy, reemplazala por tu implementación real  

# Generador de una instancia aleatoria de Set Cover
def generar_instancia(tam_min=10, tam_max=50, num_subconjuntos_max=22):
    tam_universal = random.randint(tam_min, tam_max)
    U = set(range(1, tam_universal + 1))
    subconjuntos = []

    elementos_cubiertos = set()

    while len(subconjuntos) < num_subconjuntos_max - 2:
        sub_len = random.randint(2, max(2, tam_universal // 3))
        subconjunto = set(random.sample(list(U), sub_len))
        subconjuntos.append(subconjunto)
        elementos_cubiertos.update(subconjunto)
        if elementos_cubiertos == U:
            break

    # Asegurarse de cubrir todos los elementos
    faltantes = U - elementos_cubiertos
    while faltantes:
        sub_len = min(3, len(faltantes))
        nuevo_sub = set(random.sample(list(faltantes), sub_len))
        subconjuntos.append(nuevo_sub)
        elementos_cubiertos.update(nuevo_sub)
        faltantes = U - elementos_cubiertos
    return U, subconjuntos

# Generar 50 instancias
num_instancias = 50
instancias = [generar_instancia() for _ in range(num_instancias)]

# Archivo de salida
output_file = "resultados_experimento.csv"

# Guardar en CSV
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["min_cant_subconjuntos", "conjunto_universal", "lista_subconjuntos"])
    i = 1
    for U, subconjuntos in instancias:
        print(i)
        i+=1
        resultado = dinamica_bottom_up(U, subconjuntos)[0]
        U_str = str(sorted(U))
        subconjuntos_str = str([sorted(list(s)) for s in subconjuntos])
        writer.writerow([resultado, U_str, subconjuntos_str])

print(f"✅ Archivo CSV generado con {num_instancias} instancias: {output_file}")

# Diseñar un algoritmo de búsqueda local que mejore una solución inicial. Definir qué
# constituye una vecindad y cómo se evalúan los movimientos. Explorar variantes: primero
# que mejora, mejor entre todos, etc.

# Criterio de elección: Mejor entre todos de toda la lista de subconjuntos
def busqueda_local(conjunto_universal, subconjuntos, iteraciones = float('inf')):
    elemento_inicial = max(subconjuntos, key=len) # Empiezo con el subconjunto que mas elementos tiene
    solucion_inicial = conjunto_universal.difference(elemento_inicial) # Usamos diferencia de conjuntos ya que al iterar, es mas rapido hacer comparaciones
    subsets_usados = [elemento_inicial]
    cantidad_iteraciones = min(len(subconjuntos), len(conjunto_universal), iteraciones) # Itero el minimo entre la cantidad de subconjuntos y el tamaño del conjunto universal
    i = 0
    while(i < cantidad_iteraciones and len(solucion_inicial) > 0):
        solucion_vecino = solucion_inicial.difference(subconjuntos[i])
        mejor_vecino = subconjuntos[i]
        for j in range(len(subconjuntos)): # La vecindad es el tamaño de la lista de subconjuntos
            potencial_vecino = subconjuntos[j]
            solucion_potencial_vecino = solucion_inicial.difference(potencial_vecino)
            if len(solucion_potencial_vecino) < len(solucion_vecino):
                mejor_vecino = potencial_vecino
                solucion_vecino = solucion_potencial_vecino # Elegimos la mejor solución entre todos los vecinos combinados con la solución actual
        solucion_inicial = solucion_vecino
        i += 1
        subsets_usados.append(mejor_vecino)
    return len(subsets_usados), subsets_usados, conjunto_universal.difference(solucion_inicial)

# Criterio de elección: Primero que mejore la solución
def busqueda_local_con_primera_solucion(conjunto_universal, subconjuntos, iteraciones = float('inf')):
    elemento_inicial = max(subconjuntos, key=len) # Empiezo con el subconjunto que mas elementos tiene
    solucion_inicial = conjunto_universal.difference(elemento_inicial) # Usamos diferencia de conjuntos ya que al iterar, es mas rapido hacer comparaciones
    subsets_usados = [elemento_inicial]
    cantidad_iteraciones = min(len(subconjuntos), len(conjunto_universal), iteraciones) # Itero el minimo entre la cantidad de subconjuntos y el tamaño del conjunto universal
    i = 0
    while(i < cantidad_iteraciones and len(solucion_inicial) > 0):
        vecino = subconjuntos[i]
        solucion_vecino = solucion_inicial.difference(vecino)
        if(len(solucion_vecino) < len(solucion_inicial)): # La vecindad son los elementos del rango i .. len(subconjuntos) unidos al subconjunto actual
                                                          # ya que no tiene sentido iterar sobre los subconjuntos que ya se usaron, puesto que no ofrecen mejor solución
            solucion_inicial = solucion_vecino
            subsets_usados.append(vecino)
        i += 1
    return len(subsets_usados), subsets_usados, conjunto_universal.difference(solucion_inicial)
# Diseñar un algoritmo de búsqueda local que mejore una solución inicial. Definir qué
# constituye una vecindad y cómo se evalúan los movimientos. Explorar variantes: primero
# que mejora, mejor entre todos, etc.

# Criterio de elección: Mejor entre todos de toda la lista de subconjuntos
def busqueda_local(conjunto_universal, subconjuntos):
    elemento_inicial = max(subconjuntos, key=len)
    solucion_inicial = conjunto_universal.difference(elemento_inicial)
    subsets_usados = 1
    cantidad_iteraciones = len(subconjuntos)
    i = 0
    while(i < cantidad_iteraciones and len(solucion_inicial) > 0):
        solucion_vecino = solucion_inicial.difference(subconjuntos[i])
        for j in range(len(subconjuntos)):
            potencial_vecino = subconjuntos[j]
            solucion_potencial_vecino = solucion_inicial.difference(potencial_vecino)
            if len(solucion_potencial_vecino) < len(solucion_vecino):
                solucion_vecino = solucion_potencial_vecino
        solucion_inicial = solucion_vecino
        i += 1
        subsets_usados += 1
    return subsets_usados, conjunto_universal.difference(solucion_inicial)

#
def busqueda_local_con_primera_solucion(conjunto_universal, subconjuntos):
    elemento_inicial = max(subconjuntos, key=len)
    solucion_inicial = conjunto_universal.difference(elemento_inicial)
    subsets_usados = 1
    cantidad_iteraciones = len(subconjuntos)
    i = 0
    while(i < cantidad_iteraciones and len(solucion_inicial) > 0):
        vecino = subconjuntos[i]
        solucion_vecino = solucion_inicial.difference(vecino)
        if(len(solucion_vecino) < len(solucion_inicial)):
            solucion_inicial = solucion_vecino
            subsets_usados += 1
        i += 1
    return subsets_usados, conjunto_universal.difference(solucion_inicial)
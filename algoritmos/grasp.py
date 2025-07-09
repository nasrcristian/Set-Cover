import random

def grasp(conjunto_universal, subconjuntos, cantidad_iteraciones):
    # Empiezo con conjunto infinito
    mejor_solucion = float('inf'), set(), [] # Inicializo con solución infinita para que sea reemplazada
    for i in range(cantidad_iteraciones):
        candidato = construccion_aleatorizada(subconjuntos)
        solucion_inicial = conjunto_universal.difference(candidato)
        subsets_usados = [candidato]
        cantidad_iteraciones = min(len(subconjuntos), len(conjunto_universal))
        i = 0
        while(len(solucion_inicial) > 0):
            solucion_vecino = solucion_inicial.difference(subconjuntos[i])
            mejor_vecino = subconjuntos[i]
            for j in range(len(subconjuntos)): # La vecindad es el tamaño de la lista de subconjuntos
                potencial_vecino = subconjuntos[j]
                solucion_potencial_vecino = solucion_inicial.difference(potencial_vecino)
                if len(solucion_potencial_vecino) < len(solucion_vecino):
                    mejor_vecino = potencial_vecino
                    solucion_vecino = solucion_potencial_vecino # Elegimos la mejor solución entre todos los vecinos combinados con la solución actual
            solucion_inicial = solucion_vecino
            subsets_usados.append(mejor_vecino)
            i += 1
        if(len(subsets_usados) < mejor_solucion[0]): # Elijo la mejor solución entre la previamente guardada y la de esta iteración
            mejor_solucion = len(subsets_usados), solucion_inicial, subsets_usados
        
    return len(subsets_usados), subsets_usados, conjunto_universal.difference(solucion_inicial)

# Elegimos un subconjunto al azar
def construccion_aleatorizada(subconjuntos):
    subconjunto_aleatorio = random.choice(subconjuntos)  # Elegimos un subconjunto aleatorio
    return subconjunto_aleatorio

def grasp_aleatorio(conjunto_universal, subconjuntos, cantidad_iteraciones, alpha = 0.6):
    # Empiezo con conjunto infinito
    lista_restricta_candidatos = mejores_candidatos(subconjuntos, alpha)
    mejor_solucion = float('inf'), set() # Inicializo con solución infinita para que sea reemplazada
    for i in range(cantidad_iteraciones):  # Realizamos 10 iteraciones para encontrar la mejor solución
        candidato = random.choice(lista_restricta_candidatos)
        solucion_inicial = conjunto_universal.difference(candidato) # Elegimos una solución al azar
        subsets_usados = [candidato]
        i = 0
        while(len(solucion_inicial) > 0):
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
        if(len(subsets_usados) < mejor_solucion[0]): # Elijo la mejor solución entre la previamente guardada y la de esta iteración
            mejor_solucion = len(subsets_usados), subsets_usados, solucion_inicial
        
    return len(subsets_usados), subsets_usados, conjunto_universal.difference(solucion_inicial)

def mejores_candidatos(subconjuntos, alpha):
    maximo = max(map(len, subconjuntos)) # El máximo de los subconjuntos
    piso = maximo * alpha
    candidatos = filter(lambda x: len(x) >= piso, subconjuntos) # La métrica a seguir es la cantidad de elementos cubiertos del total
    return list(candidatos) # Filtramos los subconjuntos que cumplen con el criterio de alpha

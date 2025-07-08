def dinamica_recursiva(conjunto_universal, subconjuntos):
    soluciones = dinamica_recursiva_acc(conjunto_universal, set(), subconjuntos, 0, 0)
    return soluciones[0] if soluciones else []

def dinamica_recursiva_acc(conjunto_universal, subconjunto_solucion, subconjuntos, i, subconjuntos_usados):
    if(i == len(subconjuntos)):
        return [(subconjuntos_usados, subconjunto_solucion)] if subconjunto_solucion == conjunto_universal else []  # Caso base

    subconjunto = subconjuntos[i]

    lo_uso_subconjunto = dinamica_recursiva_acc(
        conjunto_universal, 
        subconjunto_solucion.union(subconjunto), 
        subconjuntos, 
        i + 1,
        subconjuntos_usados + 1
    )

    no_lo_uso_subconjunto = dinamica_recursiva_acc(
        conjunto_universal, 
        subconjunto_solucion, 
        subconjuntos, 
        i + 1,
        subconjuntos_usados
    )

    soluciones = no_lo_uso_subconjunto + lo_uso_subconjunto

    if not soluciones:
        return []

    return [min(soluciones, key=lambda x: x[0], default=[])]

# Dinámica con memoización
def dinamica_recursiva_con_memoizacion(conjunto_universal, subconjuntos):
    memoized = [None] * len(subconjuntos)
    soluciones = dinamica_recursiva_con_memoizacion_acc(conjunto_universal, subconjuntos, 0, memoized)
    soluciones_universales = filter(lambda x: x[1] == conjunto_universal, soluciones)
    return min(soluciones_universales, key=lambda x: x[0])

def dinamica_recursiva_con_memoizacion_acc(conjunto_universal, subconjuntos, i, memoized):
    if(i == len(subconjuntos) - 1): # Caso base, recorrí todos los subconjuntos
        solucion = [[1, subconjuntos[i]], [0, set()]]
        memoized[i] = solucion # Guardo el caso base
        return solucion

    subconjunto = subconjuntos[i]

    solucionMemoizada = memoized[i + 1]

    lo_uso_subconjunto = solucionMemoizada if solucionMemoizada is not None else dinamica_recursiva_con_memoizacion_acc(
        conjunto_universal, 
        subconjuntos, 
        i + 1,
        memoized
    )

    # Se podría guardar en una variable o llamar al memoized, pero se deja por temas de comprensión
    no_lo_uso_subconjunto = solucionMemoizada if solucionMemoizada is not None else dinamica_recursiva_con_memoizacion_acc(
        conjunto_universal, 
        subconjuntos, 
        i + 1,
        memoized
    )

    lo_uso_subconjunto_con_subconjunto_actual = list(map(lambda x: [x[0] + 1, x[1].union(subconjunto)], lo_uso_subconjunto))

    soluciones = no_lo_uso_subconjunto + lo_uso_subconjunto_con_subconjunto_actual

    memoized[i] = soluciones

    return soluciones

def dinamica_bottom_up(conjunto_universal, subconjuntos):
    dp = [[]] * (len(subconjuntos) + 1) # Tabulación de 1, con listas vacías
    dp[0] = [[0, set()]]  # Caso base, no se usa ningún subconjunto

    for i in range(1, len(dp)): # Por cada subconjunto, pruebo las combinaciones de i, y los subconjuntos de i - 1, recursivamente
        soluciones_anteriores = dp[i - 1]
        subconjunto = subconjuntos[i - 1] 
        dp[i] = soluciones_anteriores + list(map(lambda x: [x[0] + 1, x[1].union(subconjunto)], soluciones_anteriores))

    soluciones_universales = filter(lambda x: x[1] == conjunto_universal, dp[len(subconjuntos)])
    return min(soluciones_universales, key=lambda x: x[0]) # Devuelvo la solución con menos subconjuntos usados, igual a universal
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

# Dinámica bottom up
def dinamica_top_down(conjunto_universal, subconjuntos):
    # TODO()
    pass
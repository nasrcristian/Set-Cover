def dinamica_recursiva(conjunto_universal, subconjuntos):
    soluciones = dinamica_recursiva_acc(conjunto_universal, set(), subconjuntos, 0, 0)
    soluciones_universales = filter(lambda x: len(conjunto_universal) == len(x[1]), soluciones)
    return min(soluciones_universales, key=lambda x: x[0], default=None)

def dinamica_recursiva_acc(conjunto_universal, subconjunto_solucion, subconjuntos, i, subconjuntos_usados):
    if(i == len(subconjuntos)):
        return [[subconjuntos_usados, subconjunto_solucion]] # Caso base

    subconjunto = subconjuntos[i]

    lo_uso_subconjuntos = dinamica_recursiva_acc(
        conjunto_universal, 
        subconjunto_solucion.union(subconjunto), 
        subconjuntos, 
        i + 1,
        subconjuntos_usados + 1
    )

    no_lo_uso_subconjuntos = dinamica_recursiva_acc(
        conjunto_universal, 
        subconjunto_solucion, 
        subconjuntos, 
        i + 1,
        subconjuntos_usados
    )

    return lo_uso_subconjuntos + no_lo_uso_subconjuntos

# Dinámica bottom up
def dinamica_top_down(conjunto_universal, subconjuntos):
    # TODO()
    pass
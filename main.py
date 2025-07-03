from algoritmos.dinamica import dinamica_recursiva, dinamica_recursiva_con_memoizacion, dinamica_bottom_up
from algoritmos.busqueda_local import busqueda_local, busqueda_local_con_primera_solucion

if __name__ == "__main__":
    print(
        dinamica_bottom_up(      
            {1, 2, 3, 4, 5},
            [{1, 2}, {3, 4}, {4, 5}, {1, 3}, {2, 3, 4}, {1, 5}, {5, 4}, {1, 3}, {1}, {4}, {3}, {2}, set()] )
        )

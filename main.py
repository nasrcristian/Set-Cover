from algoritmos.dinamica import dinamica_recursiva
from algoritmos.busqueda_local import busqueda_local, busqueda_local_con_primera_solucion

if __name__ == "__main__":
    print(
        busqueda_local_con_primera_solucion(      
            {1, 2, 3, 4, 5},
            [{1, 2}, {3, 4}, {4, 5}, {1, 3}, {2, 3, 4}, {1, 5}] )
        )

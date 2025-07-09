from algoritmos.dinamica import dinamica_recursiva, dinamica_recursiva_con_memoizacion, dinamica_bottom_up
from algoritmos.busqueda_local import busqueda_local, busqueda_local_con_primera_solucion
from algoritmos.grasp import grasp, grasp_aleatorio

soluciones = [(    {100, 101, 102, 103, 104, 105},
    [{100, 101}, {102, 103}, {104}, {105}, {100, 102}, {101, 104}, {103, 105}, {100, 105}, {101, 103}, {102}, {104, 105}]
), ( {10, 11, 12, 13, 14, 15},
    [{10, 11}, {12, 13}, {14}, {15}, {10, 12}, {11, 13}, {14, 15}, {10, 14}, {12, 15}, {11, 12}, {13}, {15}]
), ( {21, 22, 23, 24, 25, 26, 27},
    [{21, 22}, {23, 24, 25}, {26}, {27}, {22, 23, 26}, {21, 25}, {24, 26, 27}, {23, 27}, {21}, {22, 24}]
), (  {100, 101, 102, 103, 104, 105},
    [{100, 101}, {102, 103}, {104}, {105}, {100, 102}, {101, 104}, {103, 105}, {100, 105}, {101, 103}, {102}, {104, 105}]
), (  {31, 32, 33, 34, 35, 36},
    [{31, 32, 33}, {34, 35}, {36}, {31, 34}, {32, 35}, {33, 36}, {31, 36}, {32, 33, 34}, {35, 36}, {31}]
)]


if __name__ == "__main__":
    for sol in soluciones:
        print("usando universo:", sol[0], " con subconjuntos:", sol[1])
        print(
        "busqueda local con mejor solucion",
            busqueda_local(sol[0], sol[1]))
        print(
        "busqueda local con primera solucion",   
        busqueda_local_con_primera_solucion(sol[0], sol[1]))
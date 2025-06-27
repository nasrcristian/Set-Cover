from algoritmos.dinamica import dinamica_recursiva

if __name__ == "__main__":
    print(dinamica_recursiva(
        {1, 2, 3, 4, 5},
        [{1}, {2}, {1, 2}, {1, 2, 3}, {1, 3}, {1,2}, {1,4}, {4}, {5, 1}] 
    ))
# Nombre del Proyecto

Este proyecto implementa y compara el rendimiento de varios algoritmos para resolver el problema de cobertura de conjuntos.

<br>

## 📂 Estructura del Proyecto

El repositorio está organizado en dos directorios principales:

* **`/algoritmos`**: Contiene la implementación de los algoritmos principales.
    * `busqueda_local.py`:
        * `busqueda_local(conjunto_universal, subconjuntos, iteraciones)`
        * `busqueda_local_con_primera_solucion(conjunto_universal, subconjuntos, iteraciones)`
    * `dinamica.py`:
        * `dinamica_recursiva(conjunto_universal, subconjuntos)`
        * `dinamica_recursiva_con_memoizacion(conjunto_universal, subconjuntos)`
        * `dinamica_bottom_up(conjunto_universal, subconjuntos)`
    * `grasp.py`:
        * `grasp(conjunto_universal, subconjuntos, cantidad_iteraciones)`
        * `grasp_aleatorio(conjunto_universal, subconjuntos, cantidad_iteraciones, alpha)`

* **`/benchmarking`**: Incluye las herramientas para generar y ejecutar las pruebas de rendimiento.
    * **`/in`**: Carpeta que debe contener los archivos de entrada de datos (ej: `data.csv`).
    * **`/out`**: Carpeta donde se guardan los resultados generados por los benchmarks.
    * `benchmark.py`: Ejecuta un algoritmo específico con un conjunto de datos de entrada y genera un archivo de salida con las métricas.
    * `data_generator.py`: Genera archivos de entrada con datos aleatorios para las pruebas.

---

## 🚀 Ejecución y Benchmarking

Para ejecutar las pruebas de rendimiento que comparan los algoritmos, sigue estos pasos:

### 1. Requisitos Previos

Asegúrate de tener la siguiente estructura de carpetas y archivos antes de ejecutar el programa:

* Debe existir la carpeta **`benchmarking/in/`**.
* Dentro de `benchmarking/in/`, debe haber un archivo llamado **`data.csv`** con los datos de entrada.
* Debe existir la carpeta **`benchmarking/out/`** para almacenar los resultados.

### 2. Instalación de Dependencias

Instala las bibliotecas necesarias (`matplotlib` y `numpy`) utilizando pip.

```pip install matplotlib numpy```

### 3. Ejecución

Desde la carpeta raíz

```python -m main```
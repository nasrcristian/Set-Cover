from benchmarking.benchmark import benchmark
from algoritmos.grasp import grasp

benchmark("./data.csv", "benchmark_grasp.csv", lambda x, y: grasp(x, y, 200))
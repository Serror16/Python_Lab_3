from src.bubble_sort import bubble_sort
from src.heap_sort import heap_sort
from src.quick_sort import quick_sort_main
from src.radix_sort import radix_sort
from src.counting_sort import counting_sort
from src.bucket_sort import bucket_sort
import random
from tests.benchmark import benchmark_sorts
import json


if __name__ == "__main__":
    sizes = [100, 1000, 5000]
    arrays = {}

    for size in sizes:
        arrays[f"Random int ({size})"] = [random.randint(0, 10_000) for _ in range(size)]
        arrays[f"Sorted int ({size})"] = list(range(size))
        arrays[f"Reverse int ({size})"] = list(range(size, 0, -1))

    algs = {
        "Sorted": sorted,
        "Bubble": bubble_sort,
        "Quick": quick_sort_main,
        "Heap": heap_sort,
    }

    print("\nBenchmark (int):")
    results_int = benchmark_sorts(arrays, algs)
    print(json.dumps(results_int, indent=2))

    arrays_pos = {
        "Random Pos (1000)": [random.randint(0, 1000) for _ in range(1000)],
        "Random Pos (5000)": [random.randint(0, 5000) for _ in range(5000)]
    }
    algos_linear = {
        "Counting": counting_sort,
        "Radix": radix_sort,
        "Quick": quick_sort_main
    }
    print("\nBenchmark (int > 0):")
    results_linear = benchmark_sorts(arrays_pos, algos_linear)
    print(json.dumps(results_linear, indent=2, ensure_ascii=False))

    arrays_float = {
        "Float (0-1) 1000": [random.uniform(0.0, 1.0) for _ in range(1000)],
        "Float (0-1) 5000": [random.uniform(0.0, 1.0) for _ in range(5000)]
    }
    algos_float = {
        "Bucket": bucket_sort,
        "Quick": quick_sort_main,
        "Sorted": sorted
    }
    print("\nBenchmark (float):")
    results_float = benchmark_sorts(arrays_float, algos_float)
    print(json.dumps(results_float, indent=2, ensure_ascii=False))
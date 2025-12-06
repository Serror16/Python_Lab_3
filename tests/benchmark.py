import time
import copy
from typing import Callable, Dict, List, Any

def timeit_once(func: Callable, *args, **kwargs) -> float:
    """
    Замеряет время выполнения функции.
    Возвращает время выполнения.
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time

def benchmark_sorts(arrays: Dict[str, List[Any]], algs: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    """
    Запускает алгоритмы сортировки на различных массивах и возвращает результаты по времени.
    
    Вход:
        arrays: Dict("Имя массива": [данные])
        algos: Dict("Имя алгоритма": функция_сортировки)
        
    Выход:
        Dict ("Имя массива": Dict("Имя алгоритма": время_сек ))
    """
    results = {}

    for arr_name, arr_data in arrays.items():
        results[arr_name] = {}
        
        for algo_name, alg_func in algs.items():
            data_copy = copy.deepcopy(arr_data)
            
            try:
                exec_time = timeit_once(alg_func, data_copy)
                results[arr_name][algo_name] = round(exec_time, 6)
            except Exception as e:
                print(f"  Ошибка в {algo_name}: {e}")
                results[arr_name][algo_name] = -1

    return results

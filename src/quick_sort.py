from typing import List, Union
from random import randint

def quicksort_inplace(arr: List[Union[int, float, str]], low: int, high: int) -> List[Union[int, float, str]]:
    """
    Основная рекурсивная функция быстрой сортировки.
    """
    if low < high:
        q = partition(arr, low, high)
        quicksort_inplace(arr, low, q - 1)
        quicksort_inplace(arr, q + 1, high)

def partition(arr: List[Union[int, float, str]], low: int, high: int) -> int:
    """
    Функция разбиения с выбором случайного опорного элемента.
    """
    pivot_idx = randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    
    pivot = arr[high]

    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


def quick_sort_main(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    "Функция которая запускает процесс сортировки"
    n = len(arr)
    if n > 0:
        quicksort_inplace(arr, 0, n - 1)
    return arr
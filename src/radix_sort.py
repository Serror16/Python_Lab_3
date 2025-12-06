from typing import List
from src.counting_sort_by_digit import counting_sort_by_digit


def radix_sort(arr: List[int]) -> List[int]:
    """
    Поразрядная сортировка.
    Функция использует counting_sort_by_digit(сортировку подсчетом для однозначных чисел) для сортировки разрядов.
    """
    if not arr:
        return []

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
        
    return arr




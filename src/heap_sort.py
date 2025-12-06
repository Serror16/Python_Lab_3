from typing import List, Union

def heapify(arr: List[Union[int, float, str]], n: int, i: int) -> None:
    """
    Функция, которая преобразует кучу с корнем в i узле в максимальную кучу.
    """
    largest = i
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)


def heap_sort(a: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """
    Основная функция сортировки кучей.
    """
    if not a:
        return a
        
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]  
        heapify(a, i, 0)
        
    return a

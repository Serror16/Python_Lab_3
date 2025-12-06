import pytest
import copy
from typing import Callable, List, Union
from src.bubble_sort import bubble_sort
from src.heap_sort import heap_sort
from src.quick_sort import quick_sort_main
from src.radix_sort import radix_sort
from src.counting_sort import counting_sort
from src.bucket_sort import bucket_sort

int_test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([5, 1, 3, 5, 2, 1], [1, 1, 2, 3, 5, 5]),
    ([-5, 1, 0, -3, 2], [-5, -3, 0, 1, 2]),
    ([100, 4, 15, 301, 1], [1, 4, 15, 100, 301]),
]

float_test_cases = [
    ([], []),
    ([1.1], [1.1]),
    ([0.5, 0.1, 0.9, 0.1], [0.1, 0.1, 0.5, 0.9]),
    ([5, 1.5, 3.0, 2], [1.5, 2, 3.0, 5]),
    ([-5.5, 1.1, 0.0, -3.3, 2.2], [-5.5, -3.3, 0.0, 1.1, 2.2]),
]

str_test_cases = [
    ([], []),
    (["a"], ["a"]),
    (["cat", "dog", "bus"], ["bus", "cat", "dog"]),
    (["Apple", "Cat", "apple", "cat"], ["Apple", "Cat", "apple", "cat"]),
    (["10", "2", "100"], ["10", "100", "2"]),
    (["z", "y", "x"], ["x", "y", "z"]),
    (["b", "a", "b"], ["a", "b", "b"]),
]

int_sort_algs = [bubble_sort, heap_sort, quick_sort_main, radix_sort, counting_sort]

float_sort_algs = [bubble_sort, quick_sort_main,bucket_sort]

str_sort_algs = [bubble_sort, quick_sort_main,]


@pytest.mark.parametrize("sort_func", int_sort_algs)
@pytest.mark.parametrize("input_arr, expected_arr", int_test_cases)
def test_sort_int_cases(sort_func: Callable, input_arr: List[int], expected_arr: List[int]):
    """
    Тестирование сортировок на int.
    """
    arr_copy = copy.deepcopy(input_arr)
    
    if sort_func in [counting_sort, radix_sort] and any(x < 0 for x in arr_copy):
        pytest.skip("counting_sort и radix_sort не поддерживают отрицательные числа.")
        
    result = sort_func(arr_copy)
    assert result == expected_arr


@pytest.mark.parametrize("sort_func", float_sort_algs)
@pytest.mark.parametrize("input_arr, expected_arr", float_test_cases)
def test_sort_float_cases(sort_func: Callable, input_arr: List[Union[int, float]], expected_arr: List[Union[int, float]]):
    """
    Тестирование некоторых сортировок, на float.
    """
    arr_copy = copy.deepcopy(input_arr)
    result = sort_func(arr_copy)
    assert result == expected_arr


@pytest.mark.parametrize("sort_func", str_sort_algs)
@pytest.mark.parametrize("input_arr, expected_arr", str_test_cases)
def test_sort_str_cases(sort_func: Callable, input_arr: List[str], expected_arr: List[str]):
    """
    Тестирование сортировки строк.
    """
    arr_copy = copy.deepcopy(input_arr)
    
    result = sort_func(arr_copy)
    
    assert result == expected_arr
    
    
def test_inplace_property():
    """
    Проверка, что in-place сортировки модифицируют исходный список.
    """

    arr_quick = [5, 1, 3, 2]
    original_id_quick = id(arr_quick)
    result_quick = quick_sort_main(arr_quick)
    
    assert arr_quick == [1, 2, 3, 5]
    assert id(arr_quick) == original_id_quick
    assert result_quick is arr_quick

    arr_bubble = [5, 1, 3, 2]
    original_id_bubble = id(arr_bubble)
    result_bubble = bubble_sort(arr_bubble)
    
    assert arr_bubble == [1, 2, 3, 5]
    assert id(arr_bubble) == original_id_bubble
    assert result_bubble is arr_bubble

    arr_heap = [5, 1, 3, 2]
    original_id_heap = id(arr_heap)
    result_heap = heap_sort(arr_heap)
    
    assert arr_heap == [1, 2, 3, 5]
    assert id(arr_heap) == original_id_heap
    assert result_heap is arr_heap

    arr_count = [5, 1, 3, 2]
    original_id_count = id(arr_count)
    result_count = counting_sort(arr_count)
    
    assert result_count == [1, 2, 3, 5]
    assert arr_count == [5, 1, 3, 2]
    assert id(arr_count) == original_id_count
    assert result_count is not arr_count
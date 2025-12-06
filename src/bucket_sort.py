from typing import List, Optional, Union
import math
from src.quick_sort import quick_sort_main 

DEFAULT_BUCKETS = 10 

def bucket_sort(a: List[Union[int, float]], buckets: Optional[int] = None) -> List[Union[int, float]]:
    """
    Блочная сортировка.
    Функция, которая сортирует отдельные блоки при помощи quick_sort.
    """
    if not a:
        return []
        
    num_buckets = buckets if buckets is not None else DEFAULT_BUCKETS

    min_val = float(min(a))
    max_val = float(max(a))
    n = len(a)

    if n < 2 or math.isclose(min_val, max_val):
        return a

    range_val = max_val - min_val
    buckets_list = [[] for _ in range(num_buckets)]

    for x in a:
        if math.isclose(x, max_val) and range_val > 0:
            index = num_buckets - 1
        elif range_val > 0:
            index = math.floor((x - min_val) * num_buckets / range_val)
        else:
            index = 0 
        
        buckets_list[index].append(x)

    current_index = 0
    for bucket in buckets_list:
        if bucket:
            quick_sort_main(bucket)
            for item in bucket:
                a[current_index] = item
                current_index += 1

    return a
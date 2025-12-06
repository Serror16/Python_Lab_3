from typing import List

def counting_sort_by_digit(arr: List[int], exp: int) -> None:
    """
    Вспомогательная функция для radix_sort.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10


    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10

        index = count[digit] - 1
        output[index] = arr[i]

        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]

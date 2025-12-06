def factorial_recursive(n: int) -> int:
    """
    Вычисляет факториал числа n рекурсивным методом.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел.")
        
    if n == 0:
        return 1
        
    return n * factorial_recursive(n - 1)

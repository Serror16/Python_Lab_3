def fibo_recursive(n: int) -> int:
    """
    Вычисляет N-ое число Фибоначчи рекурсивным методом.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Числа Фибоначчи определены для неотрицательных целых чисел.")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)



def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n итеративным методом.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определен только для неотрицательных целых чисел.")
    
    if n == 0:
        return 1
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        
    return factorial


def fibo(n: int) -> int:
    """
    Вычисляет N-ое число Фибоначчи итеративным методом.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Числа Фибоначчи определены для неотрицательных целых чисел.")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    
    previous_fib, present_fib = 0, 1

    for _ in range(2, n + 1):
        next_fib = previous_fib + present_fib
        previous_fib = present_fib
        present_fib = next_fib
        
    return present_fib

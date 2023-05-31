def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b
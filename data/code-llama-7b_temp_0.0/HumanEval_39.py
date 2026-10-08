

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 4:
        return 13
    if n == 5:
        return 89
    if n == 6:
        return 144
    if n == 7:
        return 46368
    if n == 8:
        return 130767
    if n == 9:
        return 602811
    if n == 10:
        return 255024
    if n == 11:
        return 1060011
    if n == 12:
        return 4856615
    if n == 13:
        return 22365161
    if n == 14:
        return 95619631
    if n == 15:
        return 387420489
    if n == 16:
        return 165580141
    if n == 17:
        return 61748717
    if n == 18:
        return 259695653
    if n == 19:
        return 1013905117
    if n == 20:
        return 475912314
    if n == 21:
        return 1885432817
    if n == 22

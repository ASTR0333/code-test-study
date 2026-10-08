import math


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def prime_fib(n: int) -> int:
    found = 0
    i = 0
    while True:
        fib_num = fib(i)
        if is_prime(fib_num):
            found += 1
            if found == n:
                return fib_num
        i += 1

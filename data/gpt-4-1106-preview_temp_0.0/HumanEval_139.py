def special_factorial(n):
    if n <= 0:
        return 1
    factorial = 1
    result = 1
    for i in range(1, n + 1):
        factorial *= i
        result *= factorial
    return result

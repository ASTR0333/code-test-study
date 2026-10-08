def f(n):
    def factorial(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def sum_to(x):
        return sum(range(1, x + 1))

    result_list = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result_list.append(factorial(i))
        else:
            result_list.append(sum_to(i))
    return result_list

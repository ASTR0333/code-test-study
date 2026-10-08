def choose_num(x, y):
    if x > y:
        return -1
    max_even = -1
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            max_even = num
            break
    return max_even

def is_equal_to_sum_even(n):
    if n < 8 or n % 2 != 0:
        return False
    else:
        return (n - 8) % 4 == 0

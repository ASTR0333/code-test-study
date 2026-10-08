def rounded_avg(n, m):
    if n > m:
        return -1
    total_sum = sum(range(n, m + 1))
    count = m - n + 1
    average = round(total_sum / count)
    binary_average = bin(average)
    return binary_average
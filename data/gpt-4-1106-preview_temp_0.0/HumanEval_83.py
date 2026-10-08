def starts_one_ends(n):
    if n == 1:
        return 1
    else:
        # There are 9 options for the first digit (1-9) and 10^(n-2) options for the middle digits
        starts_with_1 = 1 * 10**(n-1)
        # There are 10 options for the first (n-1) digits and only 1 option for the last digit
        ends_with_1 = 10**(n-1)
        # Subtract the count of numbers that both start and end with 1 to avoid double-counting
        both = 1 * 10**(n-2)
        return starts_with_1 + ends_with_1 - both

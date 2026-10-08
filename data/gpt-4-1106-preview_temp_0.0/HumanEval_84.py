def solve(N):
    # Convert the integer to a string to iterate over its digits
    digits = str(N)
    # Calculate the sum of the digits
    sum_of_digits = sum(int(digit) for digit in digits)
    # Convert the sum to binary and return as a string
    return bin(sum_of_digits)[2:]
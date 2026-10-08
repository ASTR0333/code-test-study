
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # 1. check the input
    if N < 0 or N > 10000:
        raise ValueError('N should be between 0 and 10000')
    # 2. declare the variables
    sum_of_digits = 0
    # 3. find the sum of digits
    while N > 0:
        sum_of_digits += N % 2
        N = N // 2
    # 4. return the result
    return str(sum_of_digits)


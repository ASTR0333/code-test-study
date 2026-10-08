
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    # initialize the count of even and odd integer palindromes
    even, odd = 0, 0

    # loop through all the numbers from 1 to n
    for i in range(1, n + 1):
        # convert the number to a string
        s = str(i)

        # if the number is a palindrome
        if s == s[::-1]:
            # if the number is even
            if i % 2 == 0:
                # increment the count of even integer palindromes
                even += 1
            # otherwise, if the number is odd
            else:
                # increment the count of odd integer palindromes
                odd += 1

    # return the count of even and odd integer palindromes
    return even, odd


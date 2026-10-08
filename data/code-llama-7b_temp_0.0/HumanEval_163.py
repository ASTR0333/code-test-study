
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return generate_integers(b, a)
    if a % 2 == 1:
        a += 1
    if b % 2 == 0:
        b -= 1
    return [i for i in range(a, b + 1, 2)]


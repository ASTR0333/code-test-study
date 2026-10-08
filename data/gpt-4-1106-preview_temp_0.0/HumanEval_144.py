from fractions import Fraction

def simplify(x, n):
    # Convert string fractions to Fraction objects
    x_fraction = Fraction(x)
    n_fraction = Fraction(n)

    # Multiply the two fractions
    result = x_fraction * n_fraction

    # Check if the result is a whole number
    return result.denominator == 1

# Example usage:
# print(simplify("1/5", "5/1"))  # Output: True
# print(simplify("1/6", "2/1"))  # Output: False
# print(simplify("7/10", "10/2"))  # Output: False
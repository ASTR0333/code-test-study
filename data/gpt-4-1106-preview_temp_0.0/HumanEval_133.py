import math

def sum_squares(lst):
    # Round each element to the upper int (Ceiling)
    ceil_values = [math.ceil(x) for x in lst]
    # Calculate the sum of squares of the ceiling values
    sum_of_squares = sum(x**2 for x in ceil_values)
    return sum_of_squares

# Examples
print(sum_squares([1, 2, 3])) # Should output 14
print(sum_squares([1, 4, 9])) # Should output 98
print(sum_squares([1, 3, 5, 7])) # Should output 84
print(sum_squares([1.4, 4.2, 0])) # Should output 29
print(sum_squares([-2.4, 1, 1])) # Should output 6
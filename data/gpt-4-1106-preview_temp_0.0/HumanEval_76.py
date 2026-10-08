import math

def is_simple_power(x, n):
    if n <= 0:
        return False
    if x == 1:
        return True
    
    power = math.log(x, n)
    return math.isclose(power, round(power))

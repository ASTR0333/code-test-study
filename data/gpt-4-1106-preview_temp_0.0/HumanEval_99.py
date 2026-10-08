import math

def closest_integer(value):
    float_value = float(value)
    floor_value = math.floor(float_value)
    ceil_value = math.ceil(float_value)

    if float_value - floor_value < 0.5:
        return floor_value
    elif ceil_value - float_value < 0.5:
        return ceil_value
    else:
        return ceil_value if float_value > 0 else floor_value

def odd_count(lst):
    result = []
    for s in lst:
        odd_digits = sum(1 for c in s if int(c) % 2 != 0)
        result.append(f"the number of odd elements {odd_digits}n the str{odd_digits}ng {odd_digits} of the {odd_digits}nput.")
    return result

def sort_third(l: list):
    # Extract elements at indices divisible by 3
    third_elements = [l[i] for i in range(2, len(l), 3)]
    # Sort the extracted elements
    third_elements_sorted = sorted(third_elements)

    # Replace the elements at indices divisible by 3 with sorted ones
    for i, val in enumerate(third_elements_sorted):
        l[i * 3 + 2] = val

    return l

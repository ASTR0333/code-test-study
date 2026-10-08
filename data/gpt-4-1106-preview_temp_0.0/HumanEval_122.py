def add_elements(arr, k):
    # Initialize sum
    sum_of_elements = 0

    # Iterate over the first k elements
    for num in arr[:k]:
        # Check if the number has at most two digits
        if 0 <= num < 100:
            sum_of_elements += num

    return sum_of_elements

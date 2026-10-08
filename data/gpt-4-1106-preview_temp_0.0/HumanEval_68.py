def pluck(arr):
    # Initialize variables to store the smallest even value and its index
    smallest_even = float('inf')
    smallest_index = -1

    # Iterate over the array to find the smallest even value
    for index, value in enumerate(arr):
        # Check if the current value is even and less than the current smallest even
        if value % 2 == 0 and value < smallest_even:
            smallest_even = value
            smallest_index = index

    # If an even value was found, return it and its index
    if smallest_index != -1:
        return [smallest_even, smallest_index]
    else:
        # If no even value was found, return an empty list
        return []
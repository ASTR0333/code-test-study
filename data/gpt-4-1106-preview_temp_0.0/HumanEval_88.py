def sort_array(array):
    if not array:  # Check if the array is empty
        return []
    sorted_array = sorted(array)  # Sort the array in ascending order
    if (array[0] + array[-1]) % 2 == 0:  # Check if the sum of the first and last elements is even
        return sorted_array[::-1]  # Return the array in descending order
    else:
        return sorted_array  # Return the array in ascending order

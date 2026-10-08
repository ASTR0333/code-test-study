def maximum(arr, k):
    # Sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    # Return the first k elements
    return sorted_arr[:k]
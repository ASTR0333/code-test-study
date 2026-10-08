from collections import Counter

def search(lst):
    # Count the frequency of each number in the list
    freq = Counter(lst)
    # Initialize the result as -1
    result = -1
    # Iterate over the items in the frequency dictionary
    for number, count in freq.items():
        # Check if the count is greater than or equal to the number itself
        if count >= number:
            # Update the result with the maximum value
            result = max(result, number)
    return result
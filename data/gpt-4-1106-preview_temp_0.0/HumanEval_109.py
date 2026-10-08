n
def move_one_ball(arr):
    """
    Check if it's possible to sort the given array by right-shifting one element at most.

    :param arr: A list of integers.
    :return: True if sorting is possible, False otherwise.
    """
    # Check if the array is empty
    if not arr:
        return True

    # Initialize a variable to count the number of times the order breaks
    order_breaks = 0

    # Iterate through the array to find the number of order breaks
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            order_breaks += 1

    # Check the order between the last and first element
    if arr[-1] > arr[0]:
        order_breaks += 1

    # If there is more than one order break, it's not possible to sort by right shift
    return order_breaks <= 1

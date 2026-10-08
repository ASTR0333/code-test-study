\
def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    # Sort the list first alphabetically, then by length
    even_length_strings.sort()
    even_length_strings.sort(key=len)
    return even_length_strings

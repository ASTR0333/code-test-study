def total_match(lst1, lst2):
    # Calculate the total number of characters in each list
    total_chars_lst1 = sum(len(s) for s in lst1)
    total_chars_lst2 = sum(len(s) for s in lst2)

    # Compare the total number of characters and return the appropriate list
    if total_chars_lst1 <= total_chars_lst2:
        return lst1
    else:
        return lst2

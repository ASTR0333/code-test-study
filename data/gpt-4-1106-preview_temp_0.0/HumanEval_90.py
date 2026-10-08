def next_smallest(lst):
    unique_sorted_lst = sorted(set(lst))
    if len(unique_sorted_lst) < 2:
        return None
    else:
        return unique_sorted_lst[1]

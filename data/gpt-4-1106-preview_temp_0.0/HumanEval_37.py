def sort_even(l: list):
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices.sort()
    return [even_indices.pop(0) if i % 2 == 0 else l[i] for i in range(len(l))]

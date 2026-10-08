def make_a_pile(n):
    pile = []
    current_stones = n
    for _ in range(n):
        pile.append(current_stones)
        current_stones += 2
    return pile
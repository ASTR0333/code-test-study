def compare(game, guess):
    result = []
    for g, gs in zip(game, guess):
        result.append(abs(g - gs))
    return result
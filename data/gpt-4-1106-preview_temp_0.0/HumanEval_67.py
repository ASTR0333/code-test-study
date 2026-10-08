def fruit_distribution(s, n):
    # Extract the number of apples and oranges from the string
    parts = s.split(' ')
    num_apples = int(parts[0])
    num_oranges = int(parts[3])

    # Calculate the number of mangoes
    num_mangoes = n - num_apples - num_oranges

    return num_mangoes
def select_words(s, n):
    # Define a function to count consonants in a word
    def count_consonants(word):
        consonants = 'bcdfghjklmnpqrstvwxyz'
        return sum(1 for char in word.lower() if char in consonants)

    # Split the string into words
    words = s.split()

    # Filter words with exactly n consonants
    result = [word for word in words if count_consonants(word) == n]

    return result
def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    # Reverse the word to find the closest vowel from the right side
    reversed_word = word[::-1]
    for i in range(1, len(reversed_word) - 1):
        # Check if the current character is a vowel and is between two consonants
        if (reversed_word[i] in vowels and
                reversed_word[i - 1] not in vowels and
                reversed_word[i + 1] not in vowels):
            return reversed_word[i]
    return ''
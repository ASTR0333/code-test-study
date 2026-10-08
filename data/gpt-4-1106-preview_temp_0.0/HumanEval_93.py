def encode(message):
    vowels = 'aeiouAEIOU'
    vowel_shift = {v: chr((ord(v) - 65 + 2) % 26 + 65) if v.isupper() else chr((ord(v) - 97 + 2) % 26 + 97) for v in vowels}
    encoded_message = ''
    for char in message:
        if char in vowels:
            encoded_message += vowel_shift[char]
        else:
            encoded_message += char.swapcase()
    return encoded_message

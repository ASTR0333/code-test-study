def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shift = 2 * 2
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            offset = ord(char) - start
            encrypted_char = chr(start + (offset + shift) % 26)
            result += encrypted_char
        else:
            result += char
    return result

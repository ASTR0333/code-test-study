def hex_key(num):
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_hex_digits:
            count += 1
    return count

# Examples
print(hex_key('AB'))  # Output: 1
print(hex_key('1077E'))  # Output: 2
print(hex_key('ABED1A33'))  # Output: 4
print(hex_key('123456789ABCDEF0'))  # Output: 6
print(hex_key('2020'))  # Output: 2
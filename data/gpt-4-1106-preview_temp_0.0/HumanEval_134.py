import re

def check_if_last_char_is_a_letter(txt):
    # Check if the last character is a letter and is not preceded by a space
    return bool(re.search(r'[^\s]\b[a-zA-Z]\b\s*$', txt))

# Examples
print(check_if_last_char_is_a_letter('apple pie')) # ➞ False
print(check_if_last_char_is_a_letter('apple pi e')) # ➞ True
print(check_if_last_char_is_a_letter('apple pi e ')) # ➞ False
print(check_if_last_char_is_a_letter('')) # ➞ False
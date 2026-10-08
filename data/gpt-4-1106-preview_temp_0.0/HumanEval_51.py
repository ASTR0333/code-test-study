import re

def remove_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)
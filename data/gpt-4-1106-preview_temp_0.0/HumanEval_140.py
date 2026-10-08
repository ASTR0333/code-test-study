import re

def fix_spaces(text):
    # Replace more than 2 consecutive spaces with a dash
    text = re.sub(r' {3,}', '-', text)
    # Replace remaining spaces with underscores
    text = text.replace(' ', '_')
    return text

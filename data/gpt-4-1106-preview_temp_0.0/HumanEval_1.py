from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.

    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")
    stack = []
    result = []
    buffer = ""

    for char in paren_string:
        if char == "(":
            stack.append(char)
            buffer += char
        elif char == ")":
            if stack:
                stack.pop()
                buffer += char
            if not stack:
                result.append(buffer)
                buffer = ""

    return result

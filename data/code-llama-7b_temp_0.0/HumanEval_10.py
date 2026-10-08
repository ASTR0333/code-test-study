

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return string

    # Find the longest palindrome suffix
    i = 1
    while i < len(string) and is_palindrome(string[i:]):
        i += 1
    i -= 1

    # Reverse prefix that comes before the palindromic suffix
    prefix = string[:len(string)-i]
    rev_prefix = ''.join(reversed(prefix))

    # Append reverse of the prefix to the palindromic suffix
    return string + rev_prefix


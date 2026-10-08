
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # My solution
    # return True if string.count('[') > 0 and string.count(']') > 0 and string.count('[]') > 0 else False

    # Given solution
    if string.count('[') == 0:
        return False
    if string.count(']') == 0:
        return False
    if string.count('[]') == 0:
        return False
    return True


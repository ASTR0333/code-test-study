\
def words_string(s):
    """
    Split the string by commas and spaces and return the list of words.
    """
    import re  # Import the regular expression module.
    words = re.split(r'[\s,]+', s.strip())  # Use regular expression to split the string by spaces and commas.
    return words  # Return the list of words.

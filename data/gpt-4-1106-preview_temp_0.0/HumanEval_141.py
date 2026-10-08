import re


def file_name_check(file_name):
    # Regular expression to match the file name criteria
    pattern = r'^[a-zA-Z][a-zA-Z0-9]{0,2}\.(txt|exe|dll)$'
    # Check if the file name matches the pattern
    if re.match(pattern, file_name):
        return 'Yes'
    else:
        return 'No'

# Examples
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
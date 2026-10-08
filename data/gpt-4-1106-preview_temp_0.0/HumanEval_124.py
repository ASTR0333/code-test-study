import re

def valid_date(date):
    # Regular expression to match the date format mm-dd-yyyy
    date_pattern = re.compile(r'^(\d{2})-(\d{2})-(\d{4})$')
    match = date_pattern.match(date)

    if not match:
        # The date does not match the pattern
        return False

    month, day, year = map(int, match.groups())

    # Check if the month is valid
    if month < 1 or month > 12:
        return False

    # Days in each month
    days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # Check if the day is valid
    if day < 1 or day > days_in_month[month]:
        return False

    return True
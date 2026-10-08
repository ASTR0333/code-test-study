def compare_one(a, b):
    def parse_real_number(value):
        try:
            return float(str(value).replace(',', '.'))
        except ValueError:
            return None
    
    a_num = parse_real_number(a)
    b_num = parse_real_number(b)
    
    if a_num is None or b_num is None:
        return None
    
    if a_num > b_num:
        return a
    elif a_num < b_num:
        return b
    else:
        return None
def check_dict_case(dict):
    if not dict or not all(isinstance(key, str) for key in dict.keys()):
        return False
    return all(key.islower() for key in dict.keys()) or all(key.isupper() for key in dict.keys())

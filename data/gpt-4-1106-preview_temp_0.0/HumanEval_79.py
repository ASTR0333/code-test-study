def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]
    return f"db{binary_str}db"

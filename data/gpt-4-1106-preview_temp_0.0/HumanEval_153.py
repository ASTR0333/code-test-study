def Strongest_Extension(class_name, extensions):
    def extension_strength(ext):
        CAP = sum(1 for c in ext if c.isupper())
        SM = sum(1 for c in ext if c.islower())
        return CAP - SM

    strongest_ext = max(extensions, key=extension_strength)
    return f'{class_name}.{strongest_ext}'

# Example usage:
# print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: 'my_class.AA'
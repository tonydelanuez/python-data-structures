def unique_chars_in_string(input_string):
    chars = set()
    for c in input_string:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True
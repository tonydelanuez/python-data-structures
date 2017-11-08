def is_power_of_four(number):
    if number == 1:
        return True
    one_bits = 0
    one_bits_place = 0
    while number > 1:
        number = number >> 1
        if number % 2 == 1:
            one_bits += 1
        one_bits_place += 1
    return ((one_bits == 1) and (one_bits_place % 2 == 0))
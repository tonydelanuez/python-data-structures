def is_happy_number(number):
    while(number is not 1):
        to_string = str(number)
        num_evens = 0
        num_odds = 0
        sum_of_squares = 0
        for n in to_string:
            int_n = int(n)
            if int_n % 2 == 1: 
                num_odds += 1
            else: 
                num_evens += 1
            sum_of_squares += int_n * int_n
        if num_evens == num_odds:
            break
        number = sum_of_squares
    return (number == 1)
a = 123
b = 120
c = -123

def reverse_int(number: int) -> int:
    if type(number) != int: # if the argument provided is not an int
        return 0 
    negative = False
    if number < 0: # if argument is a negative number
        negative = True
        number = abs(number) # get absolute value (remove negative sign)
    number = str(number) # convert to string
    number = number[::-1] # reverse string
    number = int(number) # convert back to int
    if negative is True:
        number = 0 - number # get negative equivalent of the number
    if number <= -2**31 or number >= 2**31 - 1: # test if it is a 64 bit int or greater
        return 0 # if so, return 0
    return number

def test_with_positive_3_digit_int_no_zeros():
    assert reverse_int(a) == 321

def test_with_positive_3_digit_int_ending_with_zero():
    assert reverse_int(b) == 21

def test_with_negative_3_digit_int_no_zeros():
    assert reverse_int(c) == -321

def test_with_64_bit_int():
    assert reverse_int(1534236469) == 0

def test_with_string():
    assert reverse_int('howdy') == 0

def test_with_array():
    assert reverse_int([1, 2, 3]) == 0

from collections import Counter

def single_number(num_list: list[int]) -> int:
    """ Given a non-empty array of integers nums, every element
    appears twice except for one. Find that single one.
    return None if incorrect argument type is given """
    if type(num_list) != list or type(num_list[0]) != int:  # if argument given is not a list or first element is not an int
        return None
    c = Counter(num_list)  # get dictionary with key(numbers) value(how many times the number occurs)
    for num in c:  # iterate through each key in c
        if c[num] == 1:  # if there is only one
            return num  # return that number

def test_with_3_nums_returns_last():
    assert single_number([2, 2, 1]) == 1

def test_with_5_nums_returns_first():
    assert single_number([4, 1, 2, 1, 2]) == 4

def test_with_1_num_returns_only_num():
    assert single_number([1]) == 1

def test_with_string_arg():
    assert single_number('string') == None

def test_with_int_arg():
    assert single_number(1) == None

def test_with_array_of_chars_arg():
    assert single_number(['c', 'a', 'b']) == None

def test_with_array_of_strings_arg():
    assert single_number(['cow', 'cat', 'carrot', 'cap']) == None


from collections import Counter


def contains_duplicate(num_list: list[int]) -> bool:
    """ given an integer array nums, return true if any value appears
    at least twice in the array, and return false if every element is
    distinct"""
    if type(num_list) != list:  # if parameter given is not a list
        return 0
    c = Counter(num_list).values()  # creates a list of dictionary values for how many of each element
    duplicate = False
    for num in c:  # iterates through each value in the list
        if num > 1:  # if there are any duplicates
            duplicate = True
            break
    return duplicate



def test_with_same_first_and_last_element():
    assert contains_duplicate([1, 2, 3, 1]) == True

def test_with_all_unique_elements():
    assert contains_duplicate([1, 2, 3, 4]) == False

def test_with_same_first_three_elements():
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

def test_with_char_arg():
    assert contains_duplicate('a') == 0

def test_with_string_arg():
    assert contains_duplicate('string') == 0

def test_with_int_arg():
    assert contains_duplicate(123) == 0







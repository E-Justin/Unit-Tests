haystack1 = "hello"
needle1 = "ll"

haystack2 = "aaaaa"
needle2 = "bba"

haystack3 = "aaa"
needle3 = "aaaa"

haystack4 = "mississippi"
needle4 = "issip"

haystack5 = 'abababa'
needle5 = 5

# return -1 if needle does not exist within haystack
# return index of first occurrence of needle in haystack

def str_str(big_string: str, to_find: str) -> int:
    if type(big_string) != str or type(to_find) != str:
        return TypeError
    if to_find in big_string:
        return big_string.find(to_find)
    else:
        return -1

def test_with_return_of_2_second_arg_with_duplicate_letters():
    assert str_str(haystack1, needle1) == 2

def test_with_return_of_neg1():
    assert str_str(haystack2, needle2) == -1

def test_with_all_letters_same_return_0():
    assert str_str(haystack3, needle3) == -1

def test_with_most_in_second_arg_found_twice_return_4():
    assert str_str(haystack4, needle4) == 4

def test_with_2nd_arg_as_an_int():
    assert str_str(haystack5, needle5) == TypeError

def test_with_1st_arg_as_an_int():
    assert str_str(5, 'abababa') == TypeError

def test_with_both_args_as_ints():
    assert str_str(5, 5) == TypeError

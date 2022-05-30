import pytest

def count_vowels(string: str) -> int:
    if type(string) != str:
        return 0
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

def test_with_my_name():
    assert count_vowels('justin ezell') == 4

def test_with_my_uppercase_name():
    assert count_vowels('JUSTIN EZELL') == 4

def test_with_int_arguments():
    assert count_vowels(25) == 0

def test_with_array_of_chars_argument():
    assert count_vowels(['a', 'c', 'e']) == 0

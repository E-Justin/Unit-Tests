list1 = [1, 5, 9, 11, 22, 33, 99, 88, 44, 66, 55, 101]

def binary_search(num_list: list[int], to_find: int) -> bool:
    if type(num_list) != list or type(to_find) != int:  # makes sure arguments are correct types
        return 0
    num_list.sort() # sort list in ascending order
    found = False
    first = 0
    length = len(num_list)
    last = length - 1

    while first <= last: 
        mid = (first + last) // 2  # get middle w/ integer division
        if num_list[mid] == to_find:  # if we found it
            found = True
            break  # exit loop
        else:
            if to_find < num_list[mid]:
                last = mid - 1  # decrease last by 1
            else:
                first = mid + 1  # increase first by 1
    return found

def test_with_lowest_num_in_list():
    assert binary_search(list1, 1) == True

def test_with_highest_num_in_list():
    assert binary_search(list1, 101) == True

def test_with_middle_num_in_list():
    assert binary_search(list1, 55) == True

def test_with_low_num_thats_not_there():
    assert binary_search(list1, 0) == False

def test_with_arguments_switched():
    assert binary_search(0, list1) == 0

def test_with_string_as_first_argument():
    assert binary_search('string', 1) == 0

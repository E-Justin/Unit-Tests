
def alpha_sort(a_list: list) -> list:
    length = len(a_list) - 1  # length / last available index

    for i in range(length):  # iterate through list one time for each item
        list_changed = False  # flag to let program know that changes were or were not made
        for j in range(length):  # iterate through previous for loop (length * length) times
            current = a_list[j]  # get item
            after = a_list[j + 1]  # get item next to current

            if current > after:  # if items are in descending order
                a_list[j], a_list[j + 1] = a_list[j+1], a_list[j]  # switch them
                list_changed = True  # flag to let program know that changes were made
        if list_changed is False:  # if no changes were made
            break  # exit loop

    return a_list  # return sorted list


words = ['zebra', 'apple', 'corn', 'squash', 'banana', 'dill pickle', 'azle ']
letters = ['h', 'c', 'a', 'z', 'q', 'b', 'e', 'p', 't', 'd', 's']
letters_and_words = ['g', 'cow', 't', 'hot', 'texas', 'goat', 'animal', 'cake', 'c', 'beef']

def test_with_seven_items():
    assert alpha_sort(words) == ['apple', 'azle ', 'banana', 'corn', 'dill pickle', 'squash', 'zebra']

def test_with_eleven_chars():
    assert alpha_sort(letters) == ['a', 'b', 'c', 'd', 'e', 'h', 'p', 'q', 's', 't', 'z']

def test_with_ten_items_chars_and_strings():
    assert alpha_sort(letters_and_words) == ['animal', 'beef', 'c', 'cake', 'cow', 'g', 'goat', 'hot', 't', 'texas']

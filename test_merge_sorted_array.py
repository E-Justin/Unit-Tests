def merge_array(list_a, a, list_b, b):
    # get lengths
    length_a = len(list_a)
    length_b = len(list_b)

    # if we need to remove anything
    if a != length_a:
        for _ in range(length_a - a):
            list_a.pop()

    # if we need to remove anything
    if b != length_b:
        for _ in range(length_b - b):
            list_b.pop()

    # merge lists
    for num in list_b:
        list_a.append(num)

    # sort lists
    list_a.sort()

    return list_a


def test_merge_array_by_removing_3_from_first_list():
    assert merge_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]

def test_merge_array_with_one_empty_list():
    assert merge_array([1], 1, [], 0) == [1]

def test_merge_array_with_first_length_of_0():
    assert merge_array([0], 0, [1], 1) == [1]

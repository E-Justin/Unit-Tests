from collections import Counter

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]

nums5 = [2, 1]
nums6 = [1, 1]

nums7 = [1]
nums8 = [1, 1]

def intersect(list1: list[int], list2: list[int]) -> list[int]:
    intersection = []
    c = Counter(list1)
    for num in list2:
        if c[num] > 0:
            intersection.append(num)
            c[num] -= 1
    return intersection




def test_with_larger_first_arg_returns_all_of_second_arg():
    assert intersect(nums1, nums2) == [2, 2]

def test_with_smaller_first_arg_returns_part_of_first_arg():
    assert intersect(nums3, nums4) == [4, 9] or [9, 4]

def test_with_both_args_same_length():
    assert intersect(nums5, nums6) == [1]

def test_with_both_args_all_same_nums_first_shorter():
    assert intersect(nums7, nums8) == [1]


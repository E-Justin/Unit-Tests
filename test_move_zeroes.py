from collections import Counter
# first one: runtime: 683 ms
#            memory usage: 15.5 mb

''' runtime: 683 ms
#   memory usage: 15.5 mb   
def moveZeroes(self, numList: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = numList.count(0)

        for i in range(zeros):
            numList.remove(0)
            numList.append(0)

        return numLis'''

def move_zeroes(num_list: list[int]) -> list[int]:
    """runtime: 1034 ms
       memory usage: 15.9 mb
    Given an integer array nums, move all 0's to the
       end of it while maintaining the relative order of
       the non-zero elements."""
    if type(num_list) != list or type(num_list[0]) != int:  # if argument is incorrect type
        return 0  # return 0

    c = Counter(num_list)  # get dictionary of key(nums in list) : value(counters)
    zeroes = c[0]  # number of zeroes in list
    length = len(num_list)  # get length
    if length > 1 and zeroes > 0:  # if length is greater than 1 and there are 0s in list
        if length == zeroes:  # if list contains nothing but zeroes
            return num_list  # return the list given 
        while zeroes > 0:
            num_list.remove(0)  # remove zeroes one at a time
            num_list.append(0)  # append zeroes to end
            zeroes -= 1  # decrement 0 counter

    return num_list


nums1 = [0, 1, 0, 3, 12]
nums2 = [0]
nums3 = [0, 0, 0, 0, 0, 0, 0, 0]

def test_with_having_to_move_2_zeroes():
    assert move_zeroes(nums1) == [1, 3, 12, 0, 0]

def test_with_only_1_zero_in_list():
    assert move_zeroes(nums2) == [0]

def test_with_only_8_zeroes_in_list():
    assert move_zeroes(nums3) == [0, 0, 0, 0, 0, 0, 0, 0]

def test_with_list_of_chars():
    assert move_zeroes(['a', 'b', 'c', 'd', 'e']) == 0

def test_with_string_arg():
    assert move_zeroes('this is a string') == 0

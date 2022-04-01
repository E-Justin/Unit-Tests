

import tryingStuff # import file to test
import unittest # import test framework



class Test_TestBinarySearch(unittest.TestCase):
    def test_TrueIsPalindrome(self): 
        self.assertEqual(tryingStuff.isPalindrome(121), True)
    
    def test_FalseIsPalindrome(self):
        self.assertEqual(tryingStuff.isPalindrome(123), False)

    def test_TrueLongIsPalindrome(self):
        self.assertEqual(tryingStuff.isPalindrome(123321), True)
    
    def test_stringIsPalindrome(self): # string argument
        self.assertEqual(tryingStuff.isPalindrome('123321'), False)

    def test_sameNumberIsPalindrome(self): # single, repeated int
        self.assertEqual(tryingStuff.isPalindrome(00000000000000000000), True)
    
    def test_arrayIsPalindrome(self): # array (it is only supposed to take an int as an argument)
        self.assertEqual(tryingStuff.isPalindrome([1, 2, 1]), False)
    
    def test_negativeIsPalindrome(self): # negative
        self.assertEqual(tryingStuff.isPalindrome(-121), False)



if __name__ == '__main__':
    unittest.main()


""" 
def isPalindrome(x: int):
    if type(x) != int:
        return False
    if x < 0: # if the number is negative
        return False
    sX = str(x)
    sX = sX[::-1]
    sX = int(sX)
    if x == sX:
        palindrome = True
    else:
        palindrome = False
    return palindrome

print(isPalindrome(x))
"""

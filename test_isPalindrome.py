

import tryingStuff # import file to test
import unittest # import test framework



class Test_TestBinarySearch(unittest.TestCase):
    def test_TrueIsPalindrome(self): 
        self.assertEqual(tryingStuff.isPalindrome(121), True)
    
    def test_FalseIsPalindrome(self):
        self.assertEqual(tryingStuff.isPalindrome(123), False)

    def test_TrueLongIsPalindrome(self): # longer int is passed as argument
        self.assertEqual(tryingStuff.isPalindrome(123321), True)
    
    def test_stringIsPalindrome(self): # string is passed as argument
        self.assertEqual(tryingStuff.isPalindrome('123321'), False)

    def test_sameNumberIsPalindrome(self): #single, repeated number is passed as an argument
        self.assertEqual(tryingStuff.isPalindrome(00000000000000000000), True)
    
    def test_arrayIsPalindrome(self):
        self.assertEqual(tryingStuff.isPalindrome([1, 2, 1]), False)



if __name__ == '__main__':
    unittest.main()




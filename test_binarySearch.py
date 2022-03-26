import tryingStuff # import file to test
import unittest # import test framework

class Test_TestBinarySearch(unittest.TestCase):
    def test_lowBinarySearch(self): # lowest number in list
        self.assertEqual(tryingStuff.binarySearch([77,11,99,22,88,44,33,66,55,12,17,91,45,71,81,0], 0), True)
    
    def test_notPresentBinarySearch(self): # number not present in list
        self.assertEqual(tryingStuff.binarySearch([77,11,99,22,88,44,33,66,55,12,17,91,45,71,81,0], 13), False)

    def test_highBinarySearch(self): # highest number in list
        self.assertEqual(tryingStuff.binarySearch([77,11,99,22,88,44,33,66,55,12,17,91,45,71,81,0], 99), True)

    def test_midBinarySearch(self): # middle-ish number in list
        self.assertEqual(tryingStuff.binarySearch([77,11,99,22,88,44,33,66,55,12,17,91,45,71,81,0], 55), True)



if __name__ == '__main__':
    unittest.main()




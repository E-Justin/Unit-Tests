import tryingStuff
import unittest

class Test_TestRotateArray(unittest.TestCase):
    def test_rotateArray1(self):
        self.assertEqual(tryingStuff.rotateArray([-1,-100,3,99], 2), [3,99,-1,-100])
    
    def test_rotateArray2(self):
        self.assertEqual(tryingStuff.rotateArray([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])
    
    def test_rotateArray(self):
        self.assertEqual(tryingStuff.rotateArray([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])


if __name__ == '__main__':
    unittest.main()



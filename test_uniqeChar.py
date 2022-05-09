import tryingStuff
import unittest

s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"

class Test_FirstUniqueChar(unittest.TestCase):
    def test_uniqueCharSmallReturn0(self):
        self.assertEqual(tryingStuff.uniqueChar(s1), 0)
    def test_uniqueCharSmallReturn2(self):
        self.assertEqual(tryingStuff.uniqueChar(s2), 2)
    def test_uniqueCharSmallReturnNegative1(self):
        self.assertEqual(tryingStuff.uniqueChar(s3), -1)

if __name__ == '__main__':
    unittest.main()



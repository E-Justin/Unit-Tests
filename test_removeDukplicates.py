import tryingStuff # module to test
import unittest 

nums = [1,1,2]
charList = ['a', 'a', 'b', 'c']
notSortedListInts = [10, 8, 8, 1, 5]

class Test_removeDuplicates(unittest.TestCase):
    def test_removeDuplicatesShortListOfIntsOneDuplicate(self):
        self.assertEqual(tryingStuff.removeDuplicates(nums), [1,2])
    def test_removeDuplicatesShortListOfChars(self):
        self.assertEqual(tryingStuff.removeDuplicates(charList), ['a', 'b', 'c'])
    def test_removeDuplicatesShortListOfFloats(self):
        self.assertEqual(tryingStuff.removeDuplicates([1.25, 1.51, 1.98, 1.98]), [1.25, 1.51, 1.98])
    def test_removeDuplicatesNotSortedIntsOneDuplicate(self):
        self.assertEqual(tryingStuff.removeDuplicates(notSortedListInts), [1, 5, 8, 10])




if __name__ == "__main__":
    unittest.main()


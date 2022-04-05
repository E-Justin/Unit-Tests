import tryingStuff
import unittest

class Test_ContainsDuplicates(unittest.TestCase):
    def test_containsDuplicate1(self):
        self.assertEqual(tryingStuff.containsDuplicate([1,2,3,1]), True)
    
    def test_containsDuplicate2(self):
        self.assertEqual(tryingStuff.containsDuplicate([1,2,3,4]), False)

    def test_containsDuplicate3(self):
        self.assertEqual(tryingStuff.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)
    
    def test_containsDuplicate4String(self):
        self.assertEqual(tryingStuff.containsDuplicate('charli'), 0)
    
    def test_containsDuplicate5Chars(self):
        self.assertEqual(tryingStuff.containsDuplicate(['a', 'b', 'c']), 0)


if __name__ == "__main__":
    unittest.main()

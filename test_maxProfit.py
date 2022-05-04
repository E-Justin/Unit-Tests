import tryingStuff
import unittest

prices1 = [7,1,5,3,6,4]
prices2 = [1,2,3,4,5]
prices3 = [7,6,4,3,1]
prices4 = [7]
prices5 = 7
prices6 = 'c'

class Test_TestMaxProfit(unittest.TestCase):
    def test_maxProfitIs7(self):
        self.assertEqual(tryingStuff.maxProfit(prices1), 7)
    def test_maxProfitIs4(self):
        self.assertEqual(tryingStuff.maxProfit(prices2), 4)
    def test_maxProfitIs0(self):
        self.assertEqual(tryingStuff.maxProfit(prices3), 0)
    def test_maxProfitIs0OnlyOneNumberInList(self):
        self.assertEqual(tryingStuff.maxProfit(prices4), 0)
    def test_maxProfitIs0IntArgument(self):
        self.assertEqual(tryingStuff.maxProfit(prices5), 0)
    def test_maxProfitIs0CharArgument(self):
        self.assertEqual(tryingStuff.maxProfit(prices6), 0)

if __name__ == '__main__':
    unittest.main()

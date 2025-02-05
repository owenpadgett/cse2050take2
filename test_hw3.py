import unittest
import hw3

class TestListMethods(unittest.TestCase):

    def testListGeneration(self):
        t1, t2 = hw3.generate_lists(0)
        t3, t4 = hw3.generate_lists(1)
        t5, t6 = hw3.generate_lists(1000)

        self.assertEqual(len(t1), 0)
        self.assertEqual(len(t2), 0)
        self.assertEqual(len(t3), 1)
        self.assertEqual(len(t4), 1)
        self.assertEqual(len(t5), 1000)
        self.assertEqual(len(t6), 1000)

    def testFindCommon(self):
        t1 = [3, 2, 5, 6, 7]
        t2 = [3, 4, 6, 8, 9]

        t3 = []
        t4 = []

        self.assertEqual(hw3.find_common(t1, t2), 2)
        self.assertEqual(hw3.find_common(t3, t4), 0)

    def testFindCommonEfficient(self):
        t1 = [3, 2, 5, 6, 7]
        t2 = [3, 4, 6, 8, 9]

        t3 = []
        t4 = []

        self.assertEqual(hw3.find_common_efficient(t1, t2), 2)
        self.assertEqual(hw3.find_common_efficient(t3, t4), 0)

if __name__=="__main__":
    unittest.main()
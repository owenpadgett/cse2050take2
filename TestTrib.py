import unittest
import trib as t

class TestTrib(unittest.TestCase):
    def test_first_ten(self):
        """Tests the first 10 numbers in the tribonacci series""" 
        solutions = {1:0, 2:0, 3:1, 4:1, 5:2, 6:4, 7:7, 8:13, 9:24, 10:44} # First 10 tribs
        for k in solutions: 
            self.assertEqual(t.trib(k), solutions[k])

    def test_100th(self):
        """Tests the 100th number of the tribonacci series"""
        self.assertEqual(t.trib(100), 28992087708416717612934417)

if __name__=="__main__":
    unittest.main()
import unittest
import process as p

class TestProcess(unittest.TestCase):
    def testProcessDefault(self):
        p1 = p.Process("P1")

        self.assertEqual(p1.pid, "P1")
        self.assertEqual(p1.cycles, 100)
        self.assertEqual(p1.link, None)
        self.assertEqual(p1.prev, None)

    def testProcessCycles(self):
        p2 = p.Process("P2", 400)

        self.assertEqual(p2.pid, "P2")
        self.assertEqual(p2.cycles, 400)
        self.assertEqual(p2.link, None)
        self.assertEqual(p2.prev, None)

    def testProcessEquals(self):
        p1 = p.Process("P1")
        p2 = p.Process("P2", 400)
        p3 = p.Process("P1", 300)

        self.assertEqual(p1, p3)
        self.assertNotEqual(p1, p2)

    def testProcessRepr(self):
        p1 = p.Process("P1")

        self.assertEqual(repr(p1), "Process(P1, 100)")


if __name__ == "__main__":
    unittest.main()
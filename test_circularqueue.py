import unittest
from process import Process
from circularqueue import CircularQueue

class TestCircularQueue(unittest.TestCase):

    def test_init(self):
        """Test initializing empty and non-empty circular queues"""
        # Test empty queue
        cq = CircularQueue()
        self.assertEqual(cq._head, None)
        self.assertEqual(cq._len, 0)
        self.assertEqual(str(cq), "Empty Queue")

        # Test queue with a list of processes
        p1 = Process(pid=1, cycles=5)
        p2 = Process(pid=2, cycles=3)
        p3 = Process(pid=3, cycles=4)
        cq = CircularQueue()
        cq.add_process(p1)
        cq.add_process(p2)
        cq.add_process(p3)
        self.assertEqual(cq._len, 3)
        self.assertEqual(str(cq), "1 -> 2 -> 3")

    def test_add_process(self):
        """Test adding processes to the circular queue"""
        cq = CircularQueue()

        # Add one process
        p1 = Process(pid=1, cycles=5)
        cq.add_process(p1)
        self.assertEqual(cq._len, 1)
        self.assertEqual(str(cq), "1")

        # Add two processes
        p2 = Process(pid=2, cycles=3)
        cq.add_process(p2)
        self.assertEqual(cq._len, 2)
        self.assertEqual(str(cq), "1 -> 2")

        # Add three processes
        p3 = Process(pid=3, cycles=4)
        cq.add_process(p3)
        self.assertEqual(cq._len, 3)
        self.assertEqual(str(cq), "1 -> 2 -> 3")

    def test_repr(self):
        """Test the string representation of the queue"""
        cq = CircularQueue()
        p1 = Process(pid=1, cycles=5)
        p2 = Process(pid=2, cycles=3)
        p3 = Process(pid=3, cycles=4)
        cq.add_process(p1)
        cq.add_process(p2)
        cq.add_process(p3)
        self.assertEqual(str(cq), "1 -> 2 -> 3")

    def test_remove_process(self):
        """Test removing processes from different positions in the queue"""
        cq = CircularQueue()
        p1 = Process(pid=1, cycles=5)
        p2 = Process(pid=2, cycles=3)
        p3 = Process(pid=3, cycles=4)
        cq.add_process(p1)
        cq.add_process(p2)
        cq.add_process(p3)

        # Remove from the middle
        cq.remove_process(p2)
        self.assertEqual(cq._len, 2)
        self.assertEqual(str(cq), "1 -> 3")

        # Remove from the front
        cq.remove_process(p1)
        self.assertEqual(cq._len, 1)
        self.assertEqual(str(cq), "3")

        # Remove from the end (just before self._head)
        cq.remove_process(p3)
        self.assertEqual(cq._len, 0)
        self.assertEqual(str(cq), "Empty Queue")

        # Remove from a queue with exactly 1 process
        cq.add_process(p1)
        cq.remove_process(p1)
        self.assertEqual(cq._len, 0)
        self.assertEqual(str(cq), "Empty Queue")

    def test_kill(self):
        """Test killing a process by pid"""
        cq = CircularQueue()
        p1 = Process(pid=1, cycles=5)
        p2 = Process(pid=2, cycles=3)
        p3 = Process(pid=3, cycles=4)
        cq.add_process(p1)
        cq.add_process(p2)
        cq.add_process(p3)

        # Kill a process in the middle
        killed_process = cq.kill(2)
        self.assertEqual(killed_process.pid, 2)
        self.assertEqual(cq._len, 2)
        self.assertEqual(str(cq), "1 -> 3")

        # Kill a non-existing process (should return None)
        killed_process = cq.kill(99)
        self.assertEqual(killed_process, None)
        self.assertEqual(cq._len, 2)

if __name__ == '__main__':
    unittest.main()

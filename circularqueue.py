from process import Process

class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""
    
    def __init__(self, processes=None):
        """Initializes the circular queue."""
        self._head = None
        self._len = 0
        self._d_processes = {}  # Dictionary to store processes by pid for O(1) lookup
        
        if processes:
            for process in processes:
                self.add_process(process)

    def __len__(self):
        return self._len

    def __repr__(self):
        """Provides a string representation of the queue"""
        processes = []
        current = self._head
        if current:
            for _ in range(self._len):
                processes.append(str(current.pid))
                current = current.link
        return " -> ".join(processes) if processes else "Empty Queue"

    def add_process(self, process):
        """Adds a process to the end of the queue"""
        if self._len == 0:
            self._head = process
            process.link = process
            process.prev = process
        else:
            tail = self._head.prev
            tail.link = process
            process.prev = tail
            process.link = self._head
            self._head.prev = process

        self._d_processes[process.pid] = process
        self._len += 1

    def kill(self, pid):
        """Removes and returns a process with the given pid"""
        process = self._d_processes.get(pid)
        if not process:
            return None

        self.remove_process(process)
        return process

    def remove_process(self, process):
        """Removes and returns the given Process object from the queue"""
        if self._len == 1:
            self._head = None
        else:
            process.prev.link = process.link
            process.link.prev = process.prev
            if process == self._head:
                self._head = process.link

        del self._d_processes[process.pid]
        self._len -= 1

    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = []

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(f"{self._head.pid} finished after {n_cycles-n_remaining+1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link

            n_remaining -= 1

        return '\n'.join(return_strings)

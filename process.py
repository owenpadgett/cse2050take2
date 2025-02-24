

class Process():
    def __init__(self, pid, cycles=100):
        """Initializes a Process instance."""
        self.pid = pid
        self.cycles = cycles
        self.link = None
        self.prev = None

    def __eq__(self, other):
        """Checks equality of two Processes."""
        return self.pid == other.pid
    
    def __repr__(self):
        """Returns a useful string form of the Process."""
        return f"Process({self.pid}, {str(self.cycles)})"
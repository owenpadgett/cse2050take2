

class Process():
    def __init__(self, pid, cycles=100):
        self.pid = pid
        self.cycles = cycles
        self.link = None
        self.prev = None

    def __eq__(self, other):
        return self.pid == other.pid
    
    def __repr__(self):
        return f"Process({self.pid}, {str(self.cycles)})"
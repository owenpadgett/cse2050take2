class Entry:
    def __init__(self, item, priority):
        """Initializes an entry with an item and its priority."""
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """Defines equality based on priority."""
        if isinstance(other, Entry):
            return self.priority == other.priority
        return False

    def __lt__(self, other):
        """Defines less-than comparison based on priority."""
        if isinstance(other, Entry):
            return self.priority < other.priority
        return False

    def __le__(self, other):
        """Defines less-than-or-equal comparison based on priority."""
        if isinstance(other, Entry):
            return self.priority <= other.priority
        return False

    def __repr__(self):
        """Returns a string representation of the Entry."""
        return f"Entry(item={self.item}, priority={self.priority})"
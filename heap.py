from entry import Entry

class Heap:
    """Min-heap implementation with efficient priority updates."""

    def __init__(self):
        """Initialize an empty heap."""
        self._L = []
        self._idx = {}

    def __len__(self):
        """Return number of elements in heap."""
        return len(self._L)

    def __iter__(self):
        """Return an iterator over elements in sorted order."""
        copy = Heap()
        for entry in self._L:
            copy.insert(entry.item, entry.priority)
        while len(copy) > 0:
            yield copy.remove_min()

    def idx_parent(self, idx):
        """Return index of parent node."""
        if idx == 0:
            return None
        return (idx - 1) // 2

    def idx_left(self, idx):
        """Return index of left child."""
        left = 2 * idx + 1
        return left if left < len(self._L) else None

    def idx_right(self, idx):
        """Return index of right child."""
        right = 2 * idx + 2
        return right if right < len(self._L) else None

    def idx_min_child(self, idx):
        """Return index of child with smaller priority."""
        left = self.idx_left(idx)
        right = self.idx_right(idx)
        if left is None:
            return None
        if right is None:
            return left
        return left if self._L[left] <= self._L[right] else right

    def insert(self, item, priority):
        """Insert item with given priority."""
        if item in self._idx:
            raise ValueError(f"Item {item} already in heap")
        entry = Entry(item, priority)
        self._L.append(entry)
        idx = len(self._L) - 1
        self._idx[item] = idx
        self._upheap(idx)

    def remove_min(self):
        """Remove and return item with minimum priority."""
        if not self._L:
            raise IndexError("remove_min from empty heap")
        min_entry = self._L[0]
        last_entry = self._L.pop()
        del self._idx[min_entry.item]
        if self._L:
            self._L[0] = last_entry
            self._idx[last_entry.item] = 0
            self._downheap(0)
        return min_entry

    def change_priority(self, item, priority):
        """Change priority of an existing item."""
        if item not in self._idx:
            raise KeyError(f"Item {item} not found in heap")
        idx = self._idx[item]
        old_priority = self._L[idx].priority
        self._L[idx].priority = priority
        if priority < old_priority:
            self._upheap(idx)
        else:
            self._downheap(idx)
        return self._idx[item]

    def _swap(self, i, j):
        """Swap two elements in the heap."""
        self._L[i], self._L[j] = self._L[j], self._L[i]
        self._idx[self._L[i].item] = i
        self._idx[self._L[j].item] = j

    def _upheap(self, idx):
        """Restore heap property upwards."""
        parent = self.idx_parent(idx)
        while parent is not None and self._L[idx] < self._L[parent]:
            self._swap(idx, parent)
            idx = parent
            parent = self.idx_parent(idx)

    def _downheap(self, idx):
        """Restore heap property downwards."""
        child = self.idx_min_child(idx)
        while child is not None and self._L[child] < self._L[idx]:
            self._swap(idx, child)
            idx = child
            child = self.idx_min_child(idx)

    @staticmethod
    def heapify(entries):
        """Convert list of entries into a heap."""
        h = Heap()
        h._L = entries[:]
        h._idx = {entry.item: i for i, entry in enumerate(h._L)}
        for i in reversed(range(len(h._L) // 2)):
            h._downheap(i)
        return h
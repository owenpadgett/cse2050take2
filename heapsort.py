def idx_left(L, idx, right):
    """Returns the index of the left child of idx, or None if out of bounds."""
    left = 2 * idx + 1
    return left if left <= right else None

def idx_right(L, idx, right):
    """Returns the index of the right child of idx, or None if out of bounds."""
    right_idx = 2 * idx + 2
    return right_idx if right_idx <= right else None

def idx_max_child(L, idx, right):
    """Returns the index of the child of idx with the larger value."""
    left = idx_left(L, idx, right)
    right_ = idx_right(L, idx, right)
    
    if left is None:
        return None
    if right_ is None:
        return left
    return left if L[left] > L[right_] else right_

def swap(L, i, j):
    """Swaps elements at indices i and j in list L."""
    L[i], L[j] = L[j], L[i]

def downheap(L, idx, right):
    """Maintains max-heap property by pushing down element at idx."""
    child = idx_max_child(L, idx, right)
    while child is not None and L[child] > L[idx]:
        swap(L, idx, child)
        idx = child
        child = idx_max_child(L, idx, right)

def heapsort(L):
    """Sorts list L in-place using the heapsort algorithm."""
    n = len(L)
    
    # Heapify phase: build max-heap
    for i in reversed(range(n // 2)):
        downheap(L, i, n - 1)
    
    # Sort phase: extract max element and restore heap
    for end in reversed(range(1, n)):
        swap(L, 0, end)        # Move max to end
        downheap(L, 0, end - 1)  # Re-heapify root
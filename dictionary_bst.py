class Node:
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 1


class DictionaryBST:
    """
    A dictionary implemented using a tree for self-balancing.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Initialize the DictionaryBST.
        """
        self.root = None
        if entries:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree.
        Updates the meaning if the word already exists.
        """
        self.root = self._insert(self.root, word, meaning)

    def search(self, word):
        """
        Search for a word in the tree.
        """
        node = self._search(self.root, word)
        return node.meaning if node else None

    def print_alphabetical(self):
        """
        Return all dictionary entries in alphabetical order.
        """
        result = []
        self._in_order(self.root, result)
        return result

    def _height(self, node):
        """
        Get the height of a node.
        """
        return node.height if node else 0

    def _balance_factor(self, node):
        """
        Compute the balance factor of a node.
        """
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        """
        Update the height of a node based on its children.
        """
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        """
        Perform a right rotation.
        """
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        """
        Perform a left rotation.
        """
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def _balance(self, node):
        """
        Rebalance the tree at the given node if needed.
        """
        self._update_height(node)
        balance = self._balance_factor(node)

        # Left heavy
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right heavy
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node, word, meaning):
        """
        Recursive helper for inserting a word into the tree.
        """
        if not node:
            return Node(word, meaning)

        if word < node.word:
            node.left = self._insert(node.left, word, meaning)
        elif word > node.word:
            node.right = self._insert(node.right, word, meaning)
        else:
            node.meaning = meaning
            return node

        return self._balance(node)

    def _search(self, node, word):
        """
        Recursive helper for searching a word.
        """
        if not node:
            return None
        if word == node.word:
            return node
        elif word < node.word:
            return self._search(node.left, word)
        else:
            return self._search(node.right, word)

    def _in_order(self, node, result):
        """
        Perform an in-order traversal to collect words in order.
        """
        if node:
            self._in_order(node.left, result)
            result.append((node.word, node.meaning))
            self._in_order(node.right, result)

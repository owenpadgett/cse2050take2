from queue import Queue

class Graph:
    """Abstract base graph class."""
    def __init__(self, V=None, E=None):
        raise NotImplementedError("Graph is an abstract base class.")

    def is_connected(self, v1, v2):
        """Returns True if v1 and v2 are connected, else False."""
        return v2 in self.bfs(v1)

    def bfs(self, v):
        """Return BFS tree from vertex v as a parent dictionary."""
        visited = {v}
        tree = {v: None}
        q = Queue()
        q.put(v)
        while not q.empty():
            current = q.get()
            for neighbor in self.nbrs(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    tree[neighbor] = current
                    q.put(neighbor)
        return tree


    def shortest_path(self, v1, v2):
        """Return the shortest path between v1 and v2."""
        tree = self.bfs(v1)
        if v2 not in tree:
            return None
        path = []
        current = v2
        while current is not None:
            path.append(current)
            current = tree[current]
        path.reverse()
        return path


    def count_trees(self):
        """Returns list of trees and the number of trees in the graph."""
        visited = set()
        trees = []
        for v in self:
            if v not in visited:
                tree = self.bfs(v)
                trees.append(tree)
                visited.update(tree.keys())
        return trees, len(trees)

class AdjacencySetGraph(Graph):
    """Graph implemented using adjacency sets."""
    def __init__(self, V=None, E=None):
        self.adj = dict()
        if V:
            for v in V:
                self.add_vertex(v)
        if E:
            for e in E:
                self.add_edge(e)

    def __iter__(self):
        """Returns iterator over all vertices."""
        return iter(self.adj)

    def add_vertex(self, v):
        """Adds a vertex to the graph."""
        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, e):
        """Adds an edge to the graph."""
        a, b = e
        self.add_vertex(a)
        self.add_vertex(b)
        self.adj[a].add(b)
        self.adj[b].add(a)

    def nbrs(self, v):
        """Returns iterator over neighbors of v."""
        return iter(self.adj.get(v, set()))

class EdgeSetGraph(Graph):
    """Graph implemented using a set of edges."""
    def __init__(self, V=None, E=None):
        self.V = set(V) if V else set()
        self.E = set()
        if E:
            for e in E:
                self.add_edge(e)

    def __iter__(self):
        """Returns iterator over all vertices."""
        return iter(self.V)

    def add_vertex(self, v):
        """Adds a vertex to the graph."""
        self.V.add(v)

    def add_edge(self, e):
        """Adds an edge to the graph."""
        a, b = e
        self.add_vertex(a)
        self.add_vertex(b)
        self.E.add(tuple(sorted((a, b))))

    def nbrs(self, v):
        """Returns iterator over neighbors of v."""
        neighbors = set()
        for a, b in self.E:
            if a == v:
                neighbors.add(b)
            elif b == v:
                neighbors.add(a)
        return iter(neighbors)
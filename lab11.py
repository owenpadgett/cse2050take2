# lab11.py

class Graph_ES:
    """Graph implemented with an edge set"""

    def __init__(self, V=None, E=None):
        """Initialize with optional sets of vertices and edges"""
        self._V = set(V) if V else set()
        self._E = set(E) if E else set()

    def __len__(self):
        """Return number of vertices"""
        return len(self._V)

    def __iter__(self):
        """Iterate over vertices"""
        return iter(self._V)

    def add_vertex(self, v):
        """Add a vertex to the graph"""
        self._V.add(v)

    def remove_vertex(self, v):
        """Remove a vertex and its edges"""
        if v not in self._V:
            raise KeyError(f"{v} not in graph")
        self._V.remove(v)
        self._E = {e for e in self._E if v not in e}

    def add_edge(self, e):
        """Add an edge to the graph"""
        u, v = e
        self._V.add(u)
        self._V.add(v)
        self._E.add((u, v))

    def remove_edge(self, e):
        """Remove an edge from the graph"""
        if e not in self._E:
            raise KeyError(f"{e} not in graph")
        self._E.remove(e)

    def _neighbors(self, v):
        """Return iterator of neighbors of v"""
        return (w for (u, w) in self._E if u == v)


class Graph_AS:
    """Graph implemented with an adjacency set"""

    def __init__(self, V=None, E=None):
        """Initialize with optional sets of vertices and edges"""
        self._nbr = {}
        for v in V if V else []:
            self._nbr[v] = set()
        for u, v in E if E else []:
            self.add_edge((u, v))

    def __len__(self):
        """Return number of vertices"""
        return len(self._nbr)

    def __iter__(self):
        """Iterate over vertices"""
        return iter(self._nbr)

    def add_vertex(self, v):
        """Add a vertex to the graph"""
        if v not in self._nbr:
            self._nbr[v] = set()

    def remove_vertex(self, v):
        """Remove a vertex and its edges"""
        if v not in self._nbr:
            raise KeyError(f"{v} not in graph")
        del self._nbr[v]
        for nbrs in self._nbr.values():
            nbrs.discard(v)

    def add_edge(self, e):
        """Add an edge to the graph"""
        u, v = e
        if u not in self._nbr:
            self._nbr[u] = set()
        if v not in self._nbr:
            self._nbr[v] = set()
        self._nbr[u].add(v)

    def remove_edge(self, e):
        """Remove an edge from the graph"""
        u, v = e
        if u not in self._nbr or v not in self._nbr[u]:
            raise KeyError(f"{e} not in graph")
        self._nbr[u].remove(v)

    def _neighbors(self, v):
        """Return iterator of neighbors of v"""
        return iter(self._nbr.get(v, []))
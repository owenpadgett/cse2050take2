import unittest
from Graph import AdjacencySetGraph, EdgeSetGraph, Graph

class GraphTestFactory:
    """Factory of reusable graph tests."""

    def setUp(self):
        self.V = {'A', 'B', 'C', 'D', 'E'}
        self.E = {('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'E'), ('D', 'E')}
        self.graph = self.graph_ds(V=self.V, E=self.E)

    def test_add_vertex_and_edge(self):
        g = self.graph_ds()
        g.add_vertex('X')
        g.add_edge(('X', 'Y'))
        self.assertIn('X', list(g))
        self.assertIn('Y', list(g))
        self.assertIn('Y', list(g.nbrs('X')))

    def test_init_with_verts_and_edges(self):
        verts = set(self.graph)
        self.assertEqual(verts, self.V)
        for a, b in self.E:
            self.assertIn(b, list(self.graph.nbrs(a)))

    def test_is_connected_simple(self):
        self.assertTrue(self.graph.is_connected('A', 'E'))
        self.assertFalse(self.graph.is_connected('A', 'Z'))

    def test_is_connected_cycle(self):
        V = {'A', 'B', 'C'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'A')}
        g = self.graph_ds(V, E)
        self.assertTrue(g.is_connected('A', 'C'))

    def test_bfs(self):
        dist_from_A_expected = {'A': 0, 'B':1, 'C':1, 'E':2, 'D':3}
        tree = self.graph.bfs('A')
        dist_from_A_actual = {}
        for node in tree:
            dist = 0
            current = node
            while current is not None:
                current = tree[current]
                if current is not None:
                    dist += 1
            dist_from_A_actual[node] = dist
        self.assertEqual(dist_from_A_actual, dist_from_A_expected)

    def test_shortest_path(self):
        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}
        g = self.graph_ds(V, E)
        path = g.shortest_path('A', 'D')
        self.assertEqual(len(path) - 1, 3)

    def test_count_trees(self):
        g = self.graph_ds(V=self.V, E=self.E)
        trees, count = g.count_trees()
        all_nodes = set()
        for tree in trees:
            all_nodes.update(tree.keys())
        self.assertEqual(all_nodes, self.V)
        self.assertEqual(count, 1)

        g2 = self.graph_ds(V={'A','B','C','D','E'}, E={('A','B'),('D','E')})
        trees, count = g2.count_trees()
        tree_nodes = [set(tree.keys()) for tree in trees]
        self.assertTrue({'A', 'B'} in tree_nodes)
        self.assertTrue({'D', 'E'} in tree_nodes)
        self.assertTrue({'C'} in tree_nodes)
        self.assertEqual(count, 3)

class TestAdjacency(GraphTestFactory, unittest.TestCase):
    """Test case for AdjacencySetGraph."""
    def graph_ds(self, V=None, E=None):
        return AdjacencySetGraph(V, E)

class TestEdge(GraphTestFactory, unittest.TestCase):
    """Test case for EdgeSetGraph."""
    def graph_ds(self, V=None, E=None):
        return EdgeSetGraph(V, E)

class TestGraphInit(unittest.TestCase):
    """Test case to ensure Graph cannot be instantiated."""
    def test_init_raises(self):
        with self.assertRaises(NotImplementedError):
            Graph()

if __name__ == "__main__":
    unittest.main()
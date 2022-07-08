import random

import graph


def main():
    # test_addedge_single()
    # test_addedge_random()
    test_addedge_many_times()
    # test_searches()


def test_addedge_single():
    g = graph.Graph()

    edge = (1, 2)
    u, v = edge
    weight = 10
    g.addedge(edge, weight)
    assert u in g.vertices
    assert v in g.vertices
    assert edge in g.edges
    assert g.adjs[u] == {v}
    assert g.adjs[v] == {u}
    assert g.edgeweight((u, v)) == g.edgeweight((v, u)) == weight


def test_addedge_random():
    g = graph.Graph()
    edge_tries = 200
    minvertex, maxvertex = 0, 400
    vertices = set()

    # Build graph.
    n_edges = 0
    edges = set()
    weights = {}
    for _ in range(edge_tries):
        u = random.randint(minvertex, maxvertex)
        v = random.randint(minvertex, maxvertex)
        weight = random.randint(0, 100)
        if u != v:
            vertices.add(u)
            vertices.add(v)

            # Weight is overwritten if the edge already exists.
            weights[(u, v)] = weights[(v, u)] = weight

            if (u, v) not in edges:  # Can not sum repeated edges.
                n_edges += 1
            edges.add((u, v))
            edges.add((v, u))
        g.addedge((u, v), weight)

    assert vertices == g.vertices
    assert edges == g.edges
    assert weights == g.weights
    # We have doubled edges for non-directed graph.
    assert int(len(g.edges) / 2) == n_edges

    # Test adjacency #
    # Test len
    sumedges = 0
    for u, adjs in g.adjs.items():
        sumedges += len(adjs)
    assert len(edges) == sumedges
    # Test vertices
    for edge in edges:
        u, v = edge
        assert v in g.adjs[u]
        assert u in g.adjs[v]


def test_addedge_many_times():
    for _ in range(1000):
        test_addedge_random()


def test_searches():
    """Print outputs.
    0---1---4---7
    |   |   |   |
    2---3---5---6
    """
    g = graph.Graph()
    g.addedge((0, 1))
    g.addedge((0, 2))
    # g.addedge((1, 3))
    g.addedge((1, 4))
    g.addedge((2, 3))
    g.addedge((3, 5))
    # g.addedge((4, 5))
    g.addedge((4, 7))
    g.addedge((5, 6))
    g.addedge((6, 7))

    graph.bfs(g, 0)
    print()
    graph.dfsr(g, 0)
    print()
    graph.dfsi(g, 0)
    # graph.dfs(g, 0)


if __name__ == '__main__':
    main()

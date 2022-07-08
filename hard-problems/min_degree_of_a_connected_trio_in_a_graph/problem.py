# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
from collections import defaultdict


def create_adjacency_list(edges):
    adjacency_list = defaultdict(set)
    for edge in edges:
        u, v = edge
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)
    return adjacency_list


def get_connected_trios(adjacency_list):
    def visit(u, father, grandpa):
        visited[u] = 1
        for v in adjacency_list[u]:
            if not visited[v]:
                visit(v, u, father)
            else:
                if v == grandpa:
                    trios.add((u, father, grandpa))

    trios = set()
    vertices = adjacency_list.keys()
    visited = {u: 0 for u in adjacency_list.keys()}
    for u in vertices:
        visit(u, None, None)
    return trios


def min_trio_degree(edges):
    adjacency_list = create_adjacency_list(edges)
    connected_trios = get_connected_trios(adjacency_list)
    min_degree = float('inf')
    for connected_trio in connected_trios:
        degree = 0

        u, v, w = connected_trio
        adj_u = adjacency_list[u]
        degree += sum(1 for x in adj_u if x not in {u, v, w})

        adj_v = adjacency_list[v]
        degree += sum(1 for x in adj_v if x not in {u, v, w})
        adj_w = adjacency_list[w]
        degree += sum(1 for x in adj_w if x not in {u, v, w})
        if degree < min_degree:
            min_degree = degree

    return min_degree if min_degree != float('inf') else -1


def main():
    edges = [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]
    assert min_trio_degree(edges) == 3

    edges = [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]
    assert min_trio_degree(edges) == 0


if __name__ == '__main__':
    main()
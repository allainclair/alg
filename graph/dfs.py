import collections

#  1 -- 2 -- 6
#  |    |    |
#  3 -- 4 -- 5
graph1 = [(1, 2), (1, 3), (2, 4), (2, 6), (3, 4), (4, 5), (5, 6)]


def main():
    adjacency_list = make_adjacency_list(graph1)
    print(adjacency_list)
    dfs(adjacency_list)


def make_adjacency_list(edge_list):
    """An edge list is the definition of the graph where each tuple of the list
    is and edge from a vertex u to a vertex v.
    It returns the adjacency list of this graph.
    """
    adjacency_list = collections.defaultdict(set)
    for edge in edge_list:
        u, v = edge
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)
    return adjacency_list


def dfs(adjacency_list):
    vertices = adjacency_list.keys()
    vertex_visited_map = {u: False for u in vertices}

    def dfsutil(u):
        vertex_visited_map[u] = True
        for v in adjacency_list[u]:
            if not vertex_visited_map[v]:
                dfsutil(v)

    for vertex in vertices:
        if not vertex_visited_map[vertex]:
            dfsutil(vertex)


if __name__ == '__main__':
    main()

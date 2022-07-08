# https://leetcode.com/problems/path-with-maximum-probability/

def main():
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succ_prob = [0.5, 0.5, 0.2]
    start, end = 0, 2
    getprob(n, edges, succ_prob, 0, 2)


def getprob(n, edges, succ_prob, start, end):
    adjlist = build_adj_list(n, edges, succ_prob)
    visited_paths = {(u, ) for u in range(n)}
    paths = {u: {2, 3, 4} for u in range(n)}

    u = start
    adjs = adjlist[u]
    for adj in adjs:
        v, prob = adj
        if v in paths[u]:
            visited_paths[(u, v)]

        visited_paths[(u, v)] = prob


def build_adj_list(n, edges, succ_prob):
    adjlist = [[] for _ in range(n)]
    for edge, prob in zip(edges, succ_prob):
        u, v = edge
        print((u, v))
        print(prob)
        adjlist[u].append((v, prob))
        adjlist[v].append((u, prob))
    return adjlist


def check_paths(paths, u, v):
    pu = paths[u]
    # v = 4
    for path in pu:  # [1, 2, 3]
        if v in



if __name__ == '__main__':
    main()
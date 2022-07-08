"""https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"""


def mindist(dists):
    minindex = 0
    mindist = float('inf')
    for i, dist in enumerate(dists):
        if dist < mindist:
            mindist, minindex = dist, i
    return minindex


def dijkstra(g, source):
    vertices = set(g.vertices)
    n = len(vertices)
    dist, prev = [float('inf')]*n, [None]*n
    dist[source] = 0

    while vertices:
        u = mindist(dist)
        vertices.remove(u)

        for v in g.adjs(u):
            if v in vertices:  # Not removed yet.
                alt = dist[u] + g.weights[(u, v)]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist, prev

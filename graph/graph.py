import collections
import queue


class DiGraph:
    """Directed graph"""
    def __init__(self):
        self.adjs = collections.defaultdict(set)
        self.arcs = set()
        self.vertices = set()
        self.weights = {}

    def addarc(self, arc, weight=1):
        u, v = arc
        if u != v:  # Avoid auto loops.
            self.adjs[u].add(v)
            self.vertices |= {u, v}
            self.arcs.add((u, v))
            # Weight is overwritten if the edge already exist.
            self.weights[(u, v)] = weight
            return True
        else:
            return False

    def arcweight(self, arc):
        return self.weights[arc]


class Graph:
    """Non-directed graph"""
    def __init__(self, digraph=None):
        self.digraph = digraph or DiGraph()

    @property
    def adjs(self):
        return self.digraph.adjs

    @property
    def edges(self):
        return self.digraph.arcs

    @property
    def vertices(self):
        return self.digraph.vertices

    @property
    def weights(self):
        return self.digraph.weights

    def addedge(self, edge, weight=1):
        u, v = edge
        self.digraph.addarc((u, v), weight)
        self.digraph.addarc((v, u), weight)

    def edgeweight(self, edge):
        return self.digraph.arcweight(edge)


def bfs(graph, source):
    q = queue.SimpleQueue()
    q.put(source)
    visited = {source}
    total = 0
    while not q.empty():
        u = q.get()
        for v in graph.adjs[u]:
            total += 1
            if v not in visited:
                q.put(v)
                visited.add(v)


def dfsi(graph, source):
    """Not correct I guess."""
    stack = [source]
    visited = set()
    total = 0
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            for v in graph.adjs[u]:
                total += 1
                stack.append(v)


def dfsr(graph, source):
    def visit(u):
        visited.add(u)
        for v in graph.adjs[u]:
            if v not in visited:
                visit(v)

    visited = set()
    visit(source)

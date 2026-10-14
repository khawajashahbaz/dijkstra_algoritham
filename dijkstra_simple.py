import heapq
from collections import defaultdict


def dijkstra(graph, source):
    dist = {}
    for node in graph:
        dist[node] = float('inf')

    parent = {source: None}
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v,w in graph[u]:
            nd = d+w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, parent

def get_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent.get(target)
    return path[::-1]


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 1), ('D', 2)],
    'C': [('D', 1)],
    'D': []
}

dist, parent = dijkstra(graph, 'A')
print(dist)                    # {'A': 0, 'B': 1, 'C': 2, 'D': 3}
print(get_path(parent, 'D'))



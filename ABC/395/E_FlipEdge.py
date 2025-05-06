from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(st, size):
    INF = float('inf')
    dist = [INF] * size
    dist[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heappop(hq)
        if c > dist[v]:
            continue
        for nc, nv in g[v]:
            if c + nc >= dist[nv]:
                continue
            dist[nv] = c + nc
            heappush(hq, (c + nc, nv))
    return dist


N, M, X = map(int, input().split())
g = defaultdict(list)
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    ru, rv = u + N, v + N
    g[u].append((1, v))
    g[rv].append((1, ru))
for v in range(N):
    rv = v + N
    g[v].append((X, rv))
    g[rv].append((X, v))

dist = dijkstra(0, N * 2)
print(min(dist[N - 1], dist[N * 2 - 1]))

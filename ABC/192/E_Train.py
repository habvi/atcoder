from heapq import heappop, heappush
from collections import defaultdict

def ceil(a, b):
    return (a + b - 1) // b

def dijkstra(st):
    dist[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heappop(hq)
        if c > dist[v]:
            continue
        for nv, nt, nk in g[v]:
            nc = ceil(c, nk) * nk + nt
            if nc >= dist[nv]:
                continue
            dist[nv] = nc
            heappush(hq, (nc, nv))


n, m, X, Y = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    x, y, t, k = map(int, input().split())
    x, y = x - 1, y - 1
    g[x].append((y, t, k))
    g[y].append((x, t, k))

st = X - 1
INF = float('inf')
dist = [INF] * n
dijkstra(st)

ans = dist[Y - 1]
print(ans if ans != INF else -1)
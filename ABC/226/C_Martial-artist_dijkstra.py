from heapq import heappop, heappush
from collections import defaultdict

def dijkstra(st):
    mn = 0
    dist[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heappop(hq)
        if c > dist[v]:
            continue
        for nv in g[v]:
            nc = T[nv]
            if c + nc >= dist[nv]:
                continue
            mn += nc
            dist[nv] = c + nc
            heappush(hq, (c + nc, nv))
    return mn


N = int(input())
g = defaultdict()
T = []
for v in range(N):
    t, _, *a = map(int, input().split())
    T.append(t)
    g[v] = tuple(map(lambda x: x - 1, a))

INF = float('inf')
dist = [INF] * N
ans = T[-1] + dijkstra(N - 1)
print(ans)
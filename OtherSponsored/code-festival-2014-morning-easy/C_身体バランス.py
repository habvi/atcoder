from heapq import heappop, heappush
from collections import defaultdict

def dijkstra(st):
    dist = [INF] * n
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


n, m = map(int, input().split())
S, T = map(lambda x: int(x) - 1, input().split())

g = defaultdict(list)
for _ in range(m):
    x, y, c = map(int, input().split())
    x, y = x - 1, y - 1
    g[x].append((c, y))
    g[y].append((c, x))

INF = float('inf')
from_s = dijkstra(S)
from_t = dijkstra(T)

for v, (d, d2) in enumerate(zip(from_s, from_t)):
    if d != INF and d == d2:
        print(v + 1)
        exit()
print(-1)
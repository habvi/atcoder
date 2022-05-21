from heapq import heappop, heappush
from collections import defaultdict

def dijkstra(st):
    dist[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heappop(hq)
        if c > dist[v]:
            continue
        for nc, nv, ni in g[v]:
            if c + nc >= dist[nv]:
                continue
            pre[nv] = ni + 1
            dist[nv] = c + nc
            heappush(hq, (c + nc, nv))


n, m = map(int, input().split())
g = defaultdict(list)
for i in range(m):
    x, y, c = map(int, input().split())
    x, y = x - 1, y - 1
    g[x].append((c, y, i))
    g[y].append((c, x, i))

st = 0
INF = float('inf')
dist = [INF] * n
pre = [-1] * n
dijkstra(st)

print(*pre[1:])
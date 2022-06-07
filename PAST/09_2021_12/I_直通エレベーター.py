from heapq import heappop, heappush
from collections import defaultdict

def dijkstra(st):
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


n, m = map(int, input().split())
g = defaultdict(list)
ab = set([0, n - 1])
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((c, b))
    g[b].append((c, a))
    ab.add(a)
    ab.add(b)

ab = sorted(ab)

for i in range(len(ab) - 1):
    l, r = ab[i], ab[i + 1]
    g[l].append((r - l, r))
    g[r].append((r - l, l))

INF = float('inf')
dist = defaultdict(lambda : INF)
dijkstra(0)

print(dist[n - 1])
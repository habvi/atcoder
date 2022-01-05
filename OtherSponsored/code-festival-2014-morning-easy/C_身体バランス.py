import heapq
def dijkstra(st):
    dst = [float('inf')] * n
    dst[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heapq.heappop(hq)
        if c > dst[v]: continue
        for nc, nv in g[v]:
            if c + nc >= dst[nv]: continue
            dst[nv] = c + nc
            heapq.heappush(hq, (c + nc, nv))
    return dst

from collections import defaultdict
n, m = map(int, input().split())
s, t = map(lambda x: int(x) - 1, input().split())
g = defaultdict(list)
for _ in range(m):
    x, y, d = map(int, input().split())
    x, y = x - 1, y - 1
    g[x].append((d, y))
    g[y].append((d, x))

ds = dijkstra(s)
dt = dijkstra(t)
for i in range(n):
    if i in (s, t):
        continue
    d1, d2 = ds[i], dt[i]
    if float('inf') in (d1, d2):
        continue
    if d1 == d2:
        print(i + 1)
        exit()
print(-1)

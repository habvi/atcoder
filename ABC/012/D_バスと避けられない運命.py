from heapq import heapify, heappop, heappush
def dijkstra(u):
    hq = [(0, u)]
    heapify(hq)
    while hq:
        c, v = heappop(hq)
        if c > dist[v]: continue
        for nc, nv in G[v]:
            if c + nc >= dist[nv]: continue
            dist[nv] = c + nc
            heappush(hq, (c + nc, nv))

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    a, b = a-1, b-1
    G[a].append((t, b))
    G[b].append((t, a))

ds = []
for i in range(n):
    dist = [float('inf')] * n
    dist[i] = 0
    dijkstra(i)
    ds.append(dist)

ans = float('inf')
for i in range(n):
    for j in range(i + 1, n):
        min_ = min(max(ds[i]), max(ds[j]))
        ans = min(ans, min_)
print(ans)
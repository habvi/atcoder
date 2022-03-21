from collections import defaultdict
import heapq

def dijkstra(st):
    hq = [(0, st)]
    while hq:
        c, v = heapq.heappop(hq)
        if c > dist[v]:
            continue

        for nc, nv in g[v]:
            if c + nc >= dist[nv]:
                continue
            dist[nv] = c + nc
            heapq.heappush(hq, (c + nc, nv))


n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((c, b))

INF = float('inf')

for i in range(n):
    dist = [INF] * n
    dijkstra(i)

    mn = dist[i]
    print(mn if mn != INF else -1)
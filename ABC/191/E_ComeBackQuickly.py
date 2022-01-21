import heapq
def dijkstra(st):
    dst = [float('inf')] * n
    hq = [(0, st)]
    while hq:
        c, v = heapq.heappop(hq)
        if c > dst[v]:
            continue
        for nc, nv in g[v]:
            if c + nc >= dst[nv]:
                continue
            dst[nv] = c + nc
            heapq.heappush(hq, (c + nc, nv))
    return dst

from collections import defaultdict            
n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((c, b))

for i in range(n):
    dst = dijkstra(i)
    ans = dst[i]
    print(ans if ans != float('inf') else -1)
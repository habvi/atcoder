from collections import defaultdict
import heapq
def dijkstra(st):
    dst = defaultdict(lambda : float('inf'))
    dst[st] = 0
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

h, w = map(int, input().split())
c = [tuple(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

g = defaultdict(list)
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        g[j].append((c[i][j], i))

dst = dijkstra(1)
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == -1:
            continue        
        ans += dst[a[i][j]]
print(ans)
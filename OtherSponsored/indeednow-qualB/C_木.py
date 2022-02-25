from collections import defaultdict
from heapq import heappop, heappush

def bfs(u):
    dst = [-1] * n
    dst[u] = 0
    hq = []
    heappush(hq, u)
    while hq:
        v = heappop(hq)
        ans.append(v + 1)
        for nv in g[v]:
            if dst[nv] != -1:
                continue
            dst[nv] = dst[v] + 1
            heappush(hq, nv)
    return dst


n = int(input())

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

ans = []
bfs(0)

print(*ans)
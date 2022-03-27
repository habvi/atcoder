from heapq import heappop, heappush
from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(list)
in_deg = defaultdict(int)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    in_deg[b] += 1

hq = []
for i in range(n):
    if not in_deg[i]:
        heappush(hq, i)

ans = []
while hq:
    v = heappop(hq)
    ans.append(v + 1)
    for nv in g[v]:
        in_deg[nv] -= 1
        if not in_deg[nv]:
            heappush(hq, nv)

print(*ans if len(ans) == n else [-1])
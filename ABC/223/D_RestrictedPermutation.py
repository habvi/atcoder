from collections import defaultdict
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
g = defaultdict(list)
cnt = [0] * n
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    cnt[b] += 1

hq = []
heapify(hq)
for i in range(n):
    if not cnt[i]:
        heappush(hq, i)

ans = []
while hq:
    v = heappop(hq)
    ans.append(v + 1)
    for nv in g[v]:
        cnt[nv] -= 1
        if not cnt[nv]:
            heappush(hq, nv)

if len(ans) == n:
    print(*ans)
else:
    print(-1)
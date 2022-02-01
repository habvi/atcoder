from collections import defaultdict
from heapq import heapify, heappop, heappush

g = defaultdict(list)
enter = defaultdict(int)
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    enter[b] += 1

hq = []
heapify(hq)
for i in range(n):
    if i not in enter:
        heappush(hq, i)

dp = [0] * n
ans = 0
while hq:
    v = heappop(hq)
    for nv in g[v]:
        dp[nv] = max(dp[nv], dp[v] + 1)
        enter[nv] -= 1
        if not enter[nv]:
            heappush(hq, nv)

print(max(dp))
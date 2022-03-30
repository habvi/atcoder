from heapq import heapify, heappop, heappush
from collections import defaultdict
n, m = map(int, input().split())
day = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    if a > m:
        continue
    day[a].append(b)

hq = []
heapify(hq)
ans = 0
for i in range(1, m + 1):
    if i in day:
        for d in day[i]:
            heappush(hq, -d)
    if hq:
        ans += heappop(hq)
print(-ans)
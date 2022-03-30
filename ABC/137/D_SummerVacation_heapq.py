from heapq import heappop, heappush
from collections import defaultdict

n, m = map(int, input().split())
ab = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    if a > m:
        continue
    ab[a].append(b)

hq = []
ans = 0
for i in range(1, m + 1):
    for b in ab[i]:
        heappush(hq, -b)

    if hq:
        ans += -heappop(hq)
print(ans)
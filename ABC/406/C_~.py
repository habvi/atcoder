from collections import deque, defaultdict
from itertools import groupby

N = int(input())
INF = float('inf')
P = [INF] + list(map(lambda x: int(x) - 1, input().split()))

up = defaultdict(bool)
for i in range(1, N + 1):
    if P[i - 1] < P[i]:
        up[P[i]] = True

d = deque()
for p in P:
    if up[p]:
        d.append(1)
    else:
        d.append(0)

while d and d[0]:
    d.popleft()

tilde = []
for k, v in groupby(d):
    if k:
        tilde.append(len(list(v)))

ans = 0
for i in range(len(tilde) - 1):
    ans += tilde[i] * tilde[i + 1]
print(ans)

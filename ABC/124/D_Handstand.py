from collections import deque
from itertools import groupby

n, K = map(int, input().split())
S = input()

q = deque([])
bit = 0
total = 0
ans = 0
for k, g in groupby(S):
    lg = len(tuple(g))

    q.append((k, lg))
    total += lg
    bit += (k == '0')

    while q and bit > K:
        rb, rn = q.popleft()
        bit -= (rb == '0')
        total -= rn

    ans = max(ans, total)
print(ans)
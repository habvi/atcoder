from collections import defaultdict
from itertools import accumulate

n, m, Q = map(int, input().split())

g = defaultdict(lambda : [0] * 501)
for _ in range(m):
    l, r = map(int, input().split())
    g[l][r] += 1

for k, v in g.items():
    g[k] = list(accumulate(v))


for _ in range(Q):
    p, q = map(int, input().split())

    ans = 0
    for i in range(p, q + 1):
        ans += g[i][q] - g[i][p - 1]
    print(ans)
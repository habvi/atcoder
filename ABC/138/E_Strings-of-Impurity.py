from collections import defaultdict
from bisect import bisect

S = input()
T = input()

if set(T) - set(S):
    print(-1)
    exit()

g = defaultdict(list)
for i, s in enumerate(S):
    g[s].append(i)

now = -1
count_ = 0
for t in T:
    idx = bisect(g[t], now)

    if idx == len(g[t]):
        now = g[t][0]
        count_ += 1
    else:
        now = g[t][idx]

ans = count_ * len(S) + now + 1
print(ans)
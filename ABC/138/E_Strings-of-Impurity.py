from bisect import bisect
from collections import defaultdict

S = input()
T = input()
n = len(S)

d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)

now = -1
ans = 0
for t in T:
    if not d[t]:
        print(-1)
        exit()

    gt = bisect(d[t], now)
    if gt == len(d[t]):
        now = d[t][0]
        ans += n
    else:
        now = d[t][gt]

print(ans + now + 1)
from collections import defaultdict
from itertools import accumulate
n, k = map(int, input().split())
a = list(map(int, input().split()))
ac = list(accumulate(a))

d = defaultdict(int)
d[0] += 1
ans = 0
for c in ac:
    ans += d[c - k]
    d[c] += 1
print(ans)
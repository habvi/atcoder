from collections import Counter
from itertools import accumulate
n = int(input())
MOD = 10**9 + 7
t = [int(input()) for _ in range(n)]
t.sort()
ac = accumulate(t)
print(sum(ac))

c = Counter(t)
fac = [1]
f = 1
for i in range(1, 10001):
    f *= i
    f %= MOD
    fac.append(f)

ans = 1
for v in c.values():
    ans *= fac[v]
    ans %= MOD
print(ans)
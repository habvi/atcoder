from collections import Counter
from math import gcd

N = int(input())
MOD = 10**9 + 7

ab = []
ct = Counter()
zero2 = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a == b == 0:
        zero2 += 1
        continue
    g = gcd(a, b)
    a //= g
    b //= g
    if b == 0:
        tp = (1, 0)
    elif b > 0:
        tp = (a, b)
    else:
        tp = (-a, -b) 
    ab.append(tp)
    ct[tp] += 1

ans = 1
while ct:
    (a, b), v = ct.popitem()
    if b == 0:
        c, d = b, a
    elif a > 0:
        c, d = -b, a
    else:
        c, d = b, -a
    tmp = 1
    tmp += pow(2, v, MOD) - 1
    if (c, d) in ct:
        tmp += pow(2, ct[(c, d)]) - 1
        ct.pop((c, d))
    ans *= tmp
    ans %= MOD
print(((ans - 1 + zero2) + MOD) % MOD)
from itertools import accumulate
from math import gcd

n = int(input())
A = list(map(int, input().split()))

gcd_l = [0, *accumulate(A, gcd)]
gcd_r = [0, *accumulate(A[::-1], gcd)][::-1]

ans = 0
for i in range(n):
    ans = max(ans, gcd(gcd_l[i], gcd_r[i + 1]))
print(ans)
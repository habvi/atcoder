from math import gcd
from functools import reduce

n, K = map(int, input().split())
A = list(map(int, input().split()))

g = reduce(gcd, A)

if K <= max(A) and K % g == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
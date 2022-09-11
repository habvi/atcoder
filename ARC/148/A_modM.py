from functools import reduce
from math import gcd

N = int(input())
A = list(map(int, input().split()))

B = [abs(A[i + 1] - A[i]) for i in range(N - 1)]
g = reduce(gcd, B)

p1 = set(a % g if g else a for a in A)
p2 = set(a % 2 for a in A)
if g == 1:
    print(len(p2))
else:
    print(min(len(p1), len(p2)))
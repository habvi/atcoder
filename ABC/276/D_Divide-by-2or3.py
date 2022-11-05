from functools import reduce
from math import gcd

N = int(input())
A = list(map(int, input().split()))

g = reduce(gcd, A)
for i in range(N):
    A[i] //= g

ans = 0
for a in A:
    while a % 2 == 0:
        a //= 2
        ans += 1
    while a % 3 == 0:
        a //= 3
        ans += 1
    if a != 1:
        print(-1)
        exit()
print(ans)

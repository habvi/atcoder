from bisect import bisect, bisect_left
from itertools import accumulate

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ac_l = [0] + list(accumulate(A))
ac_r = list(accumulate(A[::-1]))[::-1] + [0]

for _ in range(Q):
    X = int(input())
    l = bisect_left(A, X)
    r = bisect(A, X)
    print(X * l - ac_l[l] + ac_r[r] - X * (N - r))
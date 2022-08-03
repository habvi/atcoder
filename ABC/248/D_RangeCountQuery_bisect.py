from bisect import bisect, bisect_left
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

B = defaultdict(list)
for i, a in enumerate(A):
    B[a].append(i + 1)

Q = int(input())
for _ in range(Q):
    L, R, X = map(int, input().split())
    l = bisect_left(B[X], L)
    r = bisect(B[X], R)
    print(r - l)

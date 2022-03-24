from bisect import bisect_left
from itertools import accumulate

n, Q = map(int, input().split())
A = [0, *map(int, input().split())]

diff = [A[i + 1] - A[i] - 1 for i in range(n)]
ac = list(accumulate(diff))

for _ in range(Q):
    K = int(input())

    i = bisect_left(ac, K)
    print(A[i] + K - ac[i - 1] * (i != 0))
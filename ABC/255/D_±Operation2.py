from bisect import bisect, bisect_left
from itertools import accumulate

n, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ac = list(accumulate(A))

for _ in range(Q):
    X = int(input())

    left = bisect_left(A, X)
    ans = X * left
    if left - 1 >= 0:
        ans -= ac[left - 1]

    right = bisect(A, X)
    num_r = n - right
    if num_r > 0:
        ans += ac[-1]
        if right - 1 >= 0:
            ans -= ac[right - 1]
        ans -= X * num_r
    print(ans)
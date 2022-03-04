from itertools import accumulate
from collections import Counter

n, k = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(k):
    B = [0] * n
    for i, a in enumerate(A):
        l = max(0, i - a)
        r = min(n, i + a + 1)
        B[l] += 1
        if r < n:
            B[r] -= 1

    A = list(accumulate(B))

    if Counter(A)[n] == n:
        break

print(*A)
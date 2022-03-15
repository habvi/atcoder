from itertools import accumulate

n, m = map(int, input().split())

A = [0] * (n + 2)
for _ in range(m):
    l, r = map(int, input().split())
    A[l] += 1
    A[r + 1] -= 1

ac = list(accumulate(A))
print(ac.count(m))
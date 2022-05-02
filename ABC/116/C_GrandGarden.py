from itertools import groupby

n = int(input())
H = list(map(int, input().split()))

ans = 0
while any(H):
    A = [k for k, _ in groupby(H)]
    A = [0, *A, 0]
    m = len(A)
    for i in range(1, m - 1):
        l, a, r = A[i - 1], A[i], A[i + 1]
        if l <= a and a >= r:
            diff = min(a - l, a - r)
            ans += diff
            A[i] -= diff
    H = A[:]
print(ans)
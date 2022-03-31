from itertools import groupby

n, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
B = [-1] * K
for k, v in groupby(A):
    for i in range(min(K, len(list(v)))):
        if B[i] + 1 != k:
            break
        B[i] = k

print(sum(B) + K)
from math import log2

n, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

m = int(log2(K)) + 1

doubling = [[0] * n for _ in range(m + 1)]
for i, a in enumerate(A):
    doubling[0][i] = a

for k in range(m):
    for i in range(n):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]

now = 0
for i in range(K.bit_length()):
    if K >> i & 1:
        now = doubling[i][now]
print(now + 1)
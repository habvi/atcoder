n, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

times = K.bit_length()

doubling = [[0] * n for _ in range(times + 1)]
for i, a in enumerate(A):
    doubling[0][i] = a

for k in range(times):
    for i in range(n):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]

now = 0
for bit in range(times):
    if K >> bit & 1:
        now = doubling[bit][now]
print(now + 1)
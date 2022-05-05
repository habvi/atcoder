n, K = map(int, input().split())
A = list(map(int, input().split()))

times = K.bit_length()
doubling = [[0] * n for _ in range(times + 1)]
total = [[0] * n for _ in range(times + 1)]

for i, a in enumerate(A):
    doubling[0][i] = (i + a) % n
    total[0][i] = a

for k in range(times):
    for i in range(n):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]
        total[k + 1][i] = total[k][i] + total[k][doubling[k][i]]

bit = []
for i in range(times):
    if K >> i & 1:
        bit.append(i)

ans = 0
x = 0
for b in bit:
    ans += total[b][x]
    x = doubling[b][x]
print(ans)
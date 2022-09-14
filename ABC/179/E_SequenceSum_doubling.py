N, X, M = map(int, input().split())

K = N
times = K.bit_length()
doubling = [[0] * M for _ in range(times + 1)]
total = [[0] * M for _ in range(times + 1)]

for i in range(M):
    doubling[0][i] = i * i % M
    total[0][i] = i

for k in range(times):
    for i in range(M):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]
        total[k + 1][i] = total[k][i] + total[k][doubling[k][i]]

ans = 0
now = X
for bit in range(times):
    if K >> bit & 1:
        ans += total[bit][now]
        now = doubling[bit][now]
print(ans)

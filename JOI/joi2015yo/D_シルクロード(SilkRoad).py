n, m = map(int, input().split())
D = [int(input()) for _ in range(n)]
C = [int(input()) for _ in range(m)]

INF = float('inf')
dp = [0] * (m + 1)

for i, d in enumerate(D):
    ndp = [INF] * (m + 1)
    for j in range(m - (n - 1)):
        if i == 0:
            ndp[i + j] = min(ndp[i + j], dp[i + j] + d * C[i + j])
        else:
            ndp[i + j] = min(ndp[i + j], dp[i + j - 1] + d * C[i + j])

    for j in range(m):
        ndp[j + 1] = min(ndp[j], ndp[j + 1])
    dp = ndp

print(dp[-1])
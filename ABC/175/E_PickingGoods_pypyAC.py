R, C, K = map(int, input().split())
g = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    r, c = r - 1, c - 1
    g[r][c] = v

dp = [[-float('inf')] * C for _ in range(4)]
dp[0][0] = 0
for i in range(R):
    for j in range(C):
        for k in reversed(range(3)):
            if dp[k][j] >= 0:
                dp[k + 1][j] = max(dp[k + 1][j], dp[k][j] + g[i][j])
        for k in range(4):
            if dp[k][j] >= 0 and j + 1 < C:
                dp[k][j + 1] = max(dp[k][j + 1], dp[k][j])

    ndp = [[-float('inf')] * C for _ in range(4)]
    for j in range(C):
        ndp[0][j] = max(ndp[0][j], dp[0][j], dp[1][j], dp[2][j], dp[3][j])
    dp = ndp
print(max(dp[0]))
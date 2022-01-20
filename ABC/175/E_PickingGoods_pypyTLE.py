R, C, K = map(int, input().split())
g = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    r, c = r - 1, c - 1
    g[r][c] = v

dp = [[[-float('inf')] * 4 for _ in range(C)] for _ in range(R)]
dp[0][0][0] = 0
for i in range(R):
    for j in range(C):
        for k in reversed(range(3)):
            if dp[i][j][k] >= 0:
                dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k] + g[i][j])
        for k in range(4):
            if dp[i][j][k] >= 0:
                if j + 1 < C:
                    dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])
                if i + 1 < R:
                    dp[i + 1][j][0] = max(dp[i + 1][j][0], dp[i][j][k])
print(max(dp[R - 1][C - 1]))
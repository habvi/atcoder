h, w = map(int, input().split())
S = [input() for _ in range(h)]
MOD = 10**9 + 7

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1

x = [[0] * w for _ in range(h)]
y = [[0] * w for _ in range(h)]
z = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if (i, j) == (0, 0) or S[i][j] == '#':
            continue

        if i - 1 >= 0:
            x[i][j] = x[i - 1][j] + dp[i - 1][j]
            x[i][j] %= MOD
        if j - 1 >= 0:
            y[i][j] = y[i][j - 1] + dp[i][j - 1]
            y[i][j] %= MOD
        if i - 1 >= 0 and j - 1 >= 0:
            z[i][j] = z[i - 1][j - 1] + dp[i - 1][j - 1]
            z[i][j] %= MOD

        dp[i][j] = x[i][j] + y[i][j] + z[i][j]
        dp[i][j] %= MOD

print(dp[h - 1][w - 1])
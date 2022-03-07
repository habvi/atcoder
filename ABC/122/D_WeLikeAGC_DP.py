n = int(input())
MOD = 10**9 + 7

dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
dp[0][3][3][3] = 1

for now in range(n):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if dp[now][i][j][k] == 0:
                    continue

                for c in range(4):
                    if (c, i, j) == (2, 1, 0) or \
                        (c, i, j) == (2, 0, 1) or \
                        (c, i, j) == (1, 2, 0) or \
                        (c, i, k) == (2, 1, 0) or \
                        (c, j, k) == (2, 1, 0):
                        continue

                    dp[now + 1][c][i][j] += dp[now][i][j][k]
                    dp[now + 1][c][i][j] %= MOD

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[n][i][j][k]
            ans %= MOD
print(ans)
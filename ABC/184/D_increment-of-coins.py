a, b, c = map(int, input().split())
dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
for i in range(99, -1, -1):
    for j in range(99, -1, -1):
        for k in range(99, -1, -1):
            sm = i + j + k
            if not sm:
                continue
            tot = 0
            tot += i / sm * (dp[i + 1][j][k] + 1)
            tot += j / sm * (dp[i][j + 1][k] + 1)
            tot += k / sm * (dp[i][j][k + 1] + 1)
            dp[i][j][k] = tot
print(dp[a][b][c])            
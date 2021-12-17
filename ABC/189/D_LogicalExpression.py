n = int(input())
dp = [[0] * 2 for i in range(n + 1)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(n):
    s = input()
    if s == 'AND':
        dp[i + 1][0 & 0] += dp[i][0]
        dp[i + 1][0 & 1] += dp[i][1]
        dp[i + 1][1 & 0] += dp[i][0]
        dp[i + 1][1 & 1] += dp[i][1]
    else:
        dp[i + 1][0 | 0] += dp[i][0]
        dp[i + 1][0 | 1] += dp[i][1]
        dp[i + 1][1 | 0] += dp[i][0]
        dp[i + 1][1 | 1] += dp[i][1]
print(dp[n][1])
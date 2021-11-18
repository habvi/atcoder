n = int(input())
dp = [[0] * 2 for _ in range(n+1)]
dp[0][0] = 1
dp[0][1] = 1

S = [input() for _ in range(n)]
for i in range(n):
    if S[i] == 'AND':
        dp[i+1][0&0] += dp[i][0]
        dp[i+1][0&1] += dp[i][1]
        dp[i+1][1&0] += dp[i][0]
        dp[i+1][1&1] += dp[i][1]
    else:
        dp[i+1][0|0] += dp[i][0]
        dp[i+1][0|1] += dp[i][1]
        dp[i+1][1|0] += dp[i][0]
        dp[i+1][1|1] += dp[i][1]
print(dp[-1][1])
n = int(input())
MOD = 10**9 + 7

dp = [0] * (n + 1)
dp[0] = 1

for i in range(3, n + 1):
    dp[i] += dp[i - 1] + dp[i - 3]
    dp[i] %= MOD

print(dp[n])
s = int(input())
MOD = 10**9 + 7
dp = [0] * (s + 1)
dp[0] = 1

for i in range(s + 1):
    for j in range(3, s + 1):
        if i + j <= s:
            dp[i + j] += dp[i]
            dp[i + j] %= MOD
print(dp[-1])
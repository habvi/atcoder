S = input()
MOD = 10**9 + 7
W = "_chokudai"

dp = [0] * len(W)
dp[0] = 1
for s in S:
    if (i := W.find(s)) != -1:
        dp[i] += dp[i - 1]
        dp[i] %= MOD
print(dp[-1])
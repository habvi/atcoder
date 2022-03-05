n = int(input())
MOD = 998244353

dp = [1] * 9

for i in range(n - 1):
    ndp = [0] * 9
    for j in range(9):
        if j == 0:
            ndp[j] = dp[0] + dp[1]
        elif j == 8:
            ndp[j] = dp[-1] + dp[-2]
        else:
            ndp[j] = dp[j - 1] + dp[j] + dp[j + 1]
        ndp[j] %= MOD

    dp = ndp

print(sum(dp) % MOD)
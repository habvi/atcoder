n = int(input())
MOD = 998244353

dp = [1] * 11
dp[0] = 0
dp[10] = 0

for _ in range(n - 1):
    ndp = [0] * 11
    for num in range(1, 10):
        ndp[num] += dp[num - 1]
        ndp[num] += dp[num]
        ndp[num] += dp[num + 1]
        ndp[num] %= MOD
    dp = ndp

print(sum(dp) % MOD)
MOD = 998244353
S = input()

n = len(S)
dp = [0] * (n + 1)
dp[0] = 1
for s in S:
    ndp = [0] * (n + 1)
    for j in range(n):
        if s in '(?' and j + 1 <= n:
            ndp[j + 1] += dp[j] % MOD
        if s in ')?' and j - 1 >= 0:
            ndp[j - 1] += dp[j] % MOD
    dp = ndp
print(dp[0] % MOD)
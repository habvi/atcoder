n, m, K = map(int, input().split())
MOD = 998244353

dp = [0] * (K + 1)
dp[0] = 1
for _ in range(n):
    ndp = [0] * (K + 1)
    for pre in range(K + 1):
        for num in range(1, m + 1):
            if pre + num <= K:
                ndp[pre + num] += dp[pre]
                ndp[pre + num] %= MOD
    dp = ndp

print(sum(dp) % MOD)
n, m, K = map(int, input().split())
MOD = 998244353

dp = [[0] * (K + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for pre in range(K + 1):
        for num in range(1, m + 1):
            if pre + num <= K:
                dp[i + 1][pre + num] += dp[i][pre]
                dp[i + 1][pre + num] %= MOD

print(sum(dp[-1]) % MOD)
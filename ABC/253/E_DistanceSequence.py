from itertools import accumulate

N, M, K = map(int, input().split())
MOD = 998244353

if K == 0:
    print(pow(M, N, MOD))
    exit()

dp = list(range(M + 1))
for _ in range(N - 1):
    ndp = [0] * (M + 1)
    for i in range(1, M + 1):
        ndp[i] += dp[-1]
        minus = dp[min(i + K - 1, M)]
        if i - K >= 0:
            minus -= dp[i - K]
        ndp[i] -= minus
        ndp[i] %= MOD
    dp = list(accumulate(ndp))
print(dp[-1] % MOD)
from itertools import accumulate

n, m, K = map(int, input().split())
MOD = 998244353

dp = [0] * (m + 1)
for i in range(1, m + 1):
    if i + K <= m:
        dp[i + K] = 1
    if i - K >= 1:
        dp[i - K] = 1

for _ in range(1, n):
    ndp = [0] * (m + 1)
    for num in range(1, m + 1):
        if num - K >= 1:
            ndp[1] += dp[num]
            ndp[1] %= MOD
            if K == 0:
                continue
            if num - K + 1 <= m:
                ndp[num - K + 1] -= dp[num]
                ndp[num - K + 1] %= MOD
        if num + K <= m:
            ndp[num + K] += dp[num]
            ndp[num + K] %= MOD
    dp = list(accumulate(ndp))

print(sum(dp) % MOD)
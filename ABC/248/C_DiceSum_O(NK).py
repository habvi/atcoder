n, m, K = map(int, input().split())
MOD = 998244353

dp = [0] * (K + 2)
dp[1] = 1
for _ in range(n):
    ndp = [0] * (K + 2)
    for now in range(1, K + 2):
        ndp[now] += ndp[now - 1] + dp[now - 1] - dp[max(0, now - 1 -m)]
        ndp[now] %= MOD
    dp = ndp

print(sum(dp) % MOD)
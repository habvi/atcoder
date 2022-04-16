n, m, K = map(int, input().split())
MOD = 998244353

mx = 50 * 50
dp = [[0] * (mx + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(mx + 1):
    for j in range(n):
        for num in range(1, m + 1):
            if i + num <= mx:
                dp[j + 1][i + num] += dp[j][i]
                dp[j + 1][i + num] %= MOD

ans = 0
for i, a in enumerate(dp[-1]):
    if i > K:
        break
    ans += a
    ans %= MOD
print(ans)
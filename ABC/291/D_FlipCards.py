N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N)]

MOD = 998244353
dp = [[0] * 2 for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1
for i, (a, b) in enumerate(ab[1:], 1):
    for j in range(2):
        if ab[i - 1][j] != a:
            dp[i][0] += dp[i - 1][j]
        if ab[i - 1][j] != b:
            dp[i][1] += dp[i - 1][j]
    dp[i][0] %= MOD
    dp[i][1] %= MOD
print(sum(dp[-1]) % MOD)
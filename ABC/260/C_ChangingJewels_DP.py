N, X, Y = map(int, input().split())

# red, blue
dp = [1, 0]
for _ in range(N - 1):
    ndp = [0, 0]
    ndp[0] += dp[0]
    dp[1] += dp[0] * X
    ndp[0] += dp[1]
    ndp[1] += dp[1] * Y
    dp = ndp
print(dp[1])
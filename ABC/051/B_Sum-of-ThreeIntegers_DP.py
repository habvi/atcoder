K, S = map(int, input().split())

dp = [0] * (S + 1)
dp[0] = 1
for _ in range(3):
    ndp = [0] * (S + 1)
    for i in range(S + 1):
        ndp[i] += dp[i]
        if i - 1 >= 0:
            ndp[i] += ndp[i - 1]
        if i - K - 1 >= 0:
            ndp[i] -= dp[i - K - 1]
    dp = ndp

print(dp[-1])
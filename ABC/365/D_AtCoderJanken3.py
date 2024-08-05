N = int(input())
S = input()

dp = [0] * 3
for s in S:
    ndp = [0] * 3
    if s == "R":
        ndp[0] = max(dp[1], dp[2])
        ndp[1] = max(dp[0] + 1, dp[2] + 1)
    elif s == "P":
        ndp[1] = max(dp[0], dp[2])
        ndp[2] = max(dp[0] + 1, dp[1] + 1)
    else:
        ndp[2] = max(dp[0], dp[1])
        ndp[0] = max(dp[1] + 1, dp[2] + 1)
    dp = ndp
print(max(dp))

# DP ver.
N = int(input())
A = list(map(int, input().split()))

dp = [0, -float('inf')]
for a in A:
    ndp = [0, 0]
    ndp[0] = max(dp[0] + a, dp[1] - a)
    ndp[1] = max(dp[0] - a, dp[1] + a)
    dp = ndp
print(dp[0])

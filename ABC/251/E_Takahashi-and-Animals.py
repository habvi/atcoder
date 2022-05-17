def calc(dp):
    for a in A[1:]:
        ndp = [INF] * 2
        ndp[0] = dp[1]
        ndp[1] = min(dp[0] + a, dp[1] + a)
        dp = ndp
    return dp


n = int(input())
A = list(map(int, input().split()))

INF = float('inf')

# x : A[0]
dp = [INF] * 2
dp[0] = 0
dp1 = calc(dp)

# o : A[0]
dp = [INF] * 2
dp[1] = A[0]
dp2 = calc(dp)

print(min(dp1[1], min(dp2)))
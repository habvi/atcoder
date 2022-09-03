N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = float('inf')
dp = [-INF] * (M + 1)
dp[0] = 0
for a in A:
    ndp = [0] * (M + 1)
    for i in range(1, M + 1):
        ndp[i] = max(dp[i], dp[i - 1] + a * i)
    dp = ndp
print(dp[-1])
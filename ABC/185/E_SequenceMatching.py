n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n + 1):
    for j in range(m + 1):
        if i < n and j < m:
            if a[i] == b[j]:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
            else:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + 1)
        if i < n:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
        if j < m:
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
print(dp[n][m])
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = float('inf')
dp = [[INF] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n + 1):
    for j in range(m + 1):
        if i - 1 >= 0 and j - 1 >= 0:
            a, b = A[i - 1], B[j - 1]
            if a == b:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

        if i - 1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        if j - 1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

print(dp[n][m])
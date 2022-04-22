n, K = map(int, input().split())
H = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * n
dp[0] = 0
for i in range(n):
    for d in range(1, K + 1):
        if i - d >= 0:
            dp[i] = min(dp[i], dp[i - d] + abs(H[i] - H[i - d]))

print(dp[-1])
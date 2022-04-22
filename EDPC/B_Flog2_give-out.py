n, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    for k in range(1, K + 1):
        if i + k < n:
            dp[i + k] = min(dp[i + k], dp[i] + abs(H[i] - H[i + k]))

print(dp[-1])

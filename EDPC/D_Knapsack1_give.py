n, W = map(int, input().split())

dp = [0] * (W + 1)
for _ in range(n):
    w, v = map(int, input().split())
    for i in reversed(range(W + 1)):
        if i - w >= 0:
            dp[i] = max(dp[i], dp[i - w] + v)

print(max(dp))
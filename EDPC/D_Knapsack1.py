n, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)]

dp = [-1] * (W + 1)
dp[0] = 0

for w, v in wv:
    for i in reversed(range(W + 1)):
        if dp[i] != -1 and i + w <= W:
            dp[i + w] = max(dp[i + w], dp[i] + v)
print(max(dp))
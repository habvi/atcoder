H, W = map(int, input().split())
A = [tuple(map(lambda x: 1 if x == '+' else -1, input())) for _ in range(H)]

INF = float('inf')
dp = [[None] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if (i + j) % 2 == 0:
            dp[i][j] = -INF
        else:
            dp[i][j] = INF
dp[-1][-1] = 0

for i in reversed(range(H)):
    for j in reversed(range(W)):
        if (i + j) % 2 == 0:
            if i + 1 < H:
                dp[i][j] = max(dp[i][j], dp[i + 1][j] + A[i + 1][j])
            if j + 1 < W:
                dp[i][j] = max(dp[i][j], dp[i][j + 1] + A[i][j + 1])
        else:
            if i + 1 < H:
                dp[i][j] = min(dp[i][j], dp[i + 1][j] - A[i + 1][j])
            if j + 1 < W:
                dp[i][j] = min(dp[i][j], dp[i][j + 1] - A[i][j + 1])

ans = dp[0][0]
if ans > 0:
    print("Takahashi")
elif ans == 0:
    print("Draw")
else:
    print("Aoki")
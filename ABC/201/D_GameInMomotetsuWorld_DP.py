h, w = map(int, input().split())
a = [tuple(map(lambda x: 1 if x == '+' else 0, input())) for _ in range(h)]

dp = [[-float('inf')] * w for _ in range(h)]
dp[h - 1][w - 1] = 0
for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i + 1 < h:
            dp[i][j] = max(dp[i][j], a[i + 1][j] - dp[i + 1][j])
        if j + 1 < w:
            dp[i][j] = max(dp[i][j], a[i][j + 1] - dp[i][j + 1])

ans = dp[0][0]
if ans == 0:
    print('Draw')
elif ans > 0:
    print('Takahashi')
else:
    print('Aoki')
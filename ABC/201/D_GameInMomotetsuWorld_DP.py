h, w = map(int, input().split())
a = [list(map(lambda x : 1 if x == '+' else -1, input())) for _ in range(h)]

dp = [[-float('inf')] * w for _ in range(h)]
for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i == h - 1 and j == w - 1:
            dp[i][j] = 0
            continue
        if i + 1 < h:
            dp[i][j] = max(dp[i][j], a[i + 1][j] - dp[i + 1][j])
        if j + 1 < w:
            dp[i][j] = max(dp[i][j], a[i][j + 1] - dp[i][j + 1])

ans = dp[0][0]
if ans == 0: print('Draw')
elif ans > 0: print('Takahashi')
else: print('Aoki')
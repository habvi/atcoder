h, w, K = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())
MOD = 998244353

# (y1, x1), row, col, other
dp = [0] * 4
dp[0] = 1
for _ in range(K):
    ndp = [0] * 4
    ndp[0] += dp[1] * (w - 1) + dp[2] * (h - 1)
    ndp[1] += dp[0] + dp[1] * (w - 2) + dp[3] * (h - 1)
    ndp[2] += dp[0] + dp[2] * (h - 2) + dp[3] * (w - 1)
    ndp[3] += dp[1] + dp[2] + dp[3] * (h - 2 + w - 2)
    dp = [x % MOD for x in ndp]

if (y1, x1) == (y2, x2):
    print(dp[0])
elif y1 == y2:
    print(dp[1])
elif x1 == x2:
    print(dp[2])
else:
    print(dp[3])
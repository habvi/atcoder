n, A = map(int, input().split())
X = list(map(int, input().split()))

mx = n * A
dp = [[0] * (mx + 1) for _ in range(n + 1)]
dp[0][0] = 1

for x in X:
    ndp = [[0] * (mx + 1) for _ in range(n + 1)]
    for i in reversed(range(n)):
        for j in range(mx + 1):
            ndp[i][j] = dp[i][j]
            if j + x <= mx:
                ndp[i + 1][j + x] += dp[i][j]
    dp = ndp

ans = 0
for i in range(1, n + 1):
    ans += dp[i][i * A]
print(ans)
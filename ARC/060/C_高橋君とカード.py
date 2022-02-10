n, A = map(int, input().split())
X = list(map(int, input().split()))

mx = max(n, max(X)) * A
dp = [[[0] * (mx + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(mx + 1):
            dp[i + 1][j][k] += dp[i][j][k]
            if k + X[i] <= mx:
                dp[i + 1][j + 1][k + X[i]] += dp[i][j][k]

ans = 0
for i in range(1, n + 1):
    ans += dp[n][i][i * A]

print(ans)
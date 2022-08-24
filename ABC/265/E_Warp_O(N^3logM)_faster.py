N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
ng = set()
for _ in range(M):
    x, y= map(int, input().split())
    ng.add((x, y))
MOD = 998244353

# ef, cd, ab
dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
ans = 0
for i in range(N + 1):
    for j in range(N - i + 1):
        for k in range(N - i - j + 1):
            x = A * i + C * j + E * k
            y = B * i + D * j + F * k
            if (x, y) in ng:
                dp[i][j][k] = 0
            pre = dp[i][j][k]
            if i + j + k == N:
                ans += (pre % MOD)
            if i + 1 <= N:
                dp[i + 1][j][k] += (pre % MOD)
            if j + 1 <= N:
                dp[i][j + 1][k] += (pre % MOD)
            if k + 1 <= N:
                dp[i][j][k + 1] += (pre % MOD)
print(ans % MOD)

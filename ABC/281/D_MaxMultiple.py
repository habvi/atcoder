N, K, D = map(int, input().split())
A = list(map(int, input().split()))

INF = float('inf')
dp = [[-INF] * D for _ in range(K + 1)]
dp[0][0] = 0
for a in A:
    for i in reversed(range(K)):
        for j in reversed(range(D)):
            nxt = (j + a) % D
            dp[i + 1][nxt] = max(dp[i + 1][nxt], dp[i][j] + a)

ans = dp[-1][0]
print(ans if ans != -INF else -1)
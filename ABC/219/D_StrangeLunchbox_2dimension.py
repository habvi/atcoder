n = int(input())
x, y = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dp = [[INF] * (y + 1) for _ in range(x + 1)]
dp[0][0] = 0

for a, b in ab:
    for i in reversed(range(x + 1)):
        for j in reversed(range(y + 1)):
            ni = min(i + a, x)
            nj = min(j + b, y)
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 1)

ans = dp[x][y]
print(ans if ans != INF else -1)
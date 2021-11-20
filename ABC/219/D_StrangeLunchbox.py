n = int(input())
X, Y = map(int, input().split())
dp = [[[float('inf')]*(Y+1) for _ in range(X+1)] for _ in range(n+1)]
dp[0][0][0] = 0

ab = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for x in range(X+1):
        for y in range(Y+1):
            dp[i+1][x][y] = min(dp[i+1][x][y], dp[i][x][y])

            tk, ti = ab[i]
            dp[i+1][min(X, x+tk)][min(Y, y+ti)] = min(dp[i+1][min(X, x+tk)][min(Y, y+ti)], dp[i][x][y] + 1)

ans = dp[n][X][Y]
print(ans if ans != float('inf') else -1)
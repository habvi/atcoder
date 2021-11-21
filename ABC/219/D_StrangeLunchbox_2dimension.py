n = int(input())
X, Y = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')]*(Y+1) for _ in range(X+1)]
dp[0][0] = 0

for a, b in ab:
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            mx = min(X, i + a)
            my = min(Y, j + b)
            dp[mx][my] = min(dp[mx][my], dp[i][j] + 1)
print(dp[X][Y] if dp[X][Y] != float('inf') else -1)
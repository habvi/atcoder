def dist(x, y, z, x2, y2, z2):
    return abs(x - x2) + abs(y - y2) + max(0, z2 - z)


n = int(input())
xyz = [tuple(map(int, input().split())) for _ in range(n)]

m = 1 << n
INF = float('inf')
dp = [[INF] * n for _ in range(m)]
for i in range(1, n):
    x, y, z = xyz[0]
    x2, y2, z2 = xyz[i]
    dp[1 << i][i] = dist(x, y, z, x2, y2, z2)

for i in range(m):
    for j in range(n):
        if not i >> j & 1:
            continue

        for k in range(n):
            if j == k or i >> k & 1:
                continue
            x, y, z = xyz[j]
            x2, y2, z2 = xyz[k]
            dp[i | 1 << k][k] = min(dp[i | 1 << k][k], dp[i][j] + dist(x, y, z, x2, y2, z2))

print(dp[-1][0])
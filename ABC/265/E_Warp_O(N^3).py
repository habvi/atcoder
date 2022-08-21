N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
ng = set()
for _ in range(M):
    x, y= map(int, input().split())
    ng.add((x, y))
MOD = 998244353

dp = [[1]]
for total in range(N):
    # y, x
    ndp = [[0] * (total + 2) for _ in range(total + 2)]
    for x in range(total + 1):
        for y in range(total + 1):
            X = A * x + C * y + E * (total - x - y)
            Y = B * x + D * y + F * (total - x - y)
            for i, (dx, dy) in enumerate(((A, B), (C, D), (E, F))):
                NX, NY = X + dx, Y + dy
                if (NX, NY) in ng:
                    continue
                nx, ny = x, y
                if i == 0:
                    nx += 1
                elif i == 1:
                    ny += 1
                ndp[nx][ny] += dp[x][y]
                ndp[nx][ny] %= MOD
    dp = ndp
ans = sum(sum(x) for x in dp) % MOD
print(ans)

def cost(a, b, c, p, q, r):
    return abs(p - a) + abs(q - b) + max(0, r - c)


n = int(input())
xyz = [tuple(map(int, input().split())) for _ in range(n)]

m = 1 << n
INF = float('inf')
dp = [[INF] * n for _ in range(m)]

sx, sy, sc = xyz[0]
for nv, (p, q, r) in enumerate(xyz[1:], 1):
    dp[1 << nv][nv] = cost(sx, sy, sc, p, q, r)

for now in range(m):
    for v in range(n):
        if not now >> v & 1:
            continue

        a, b, c = xyz[v]
        for nv in range(n):
            if n == nv or now >> nv & 1:
                continue

            p, q, r = xyz[nv]
            nxt = now | 1 << nv
            dp[nxt][nv] = min(dp[nxt][nv], \
                              dp[now][v] + cost(a, b, c, p, q, r))

print(dp[-1][0])
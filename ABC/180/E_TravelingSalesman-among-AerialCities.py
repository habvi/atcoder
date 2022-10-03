from collections import defaultdict

def calc(a, b, c, p, q, r):
    return abs(p - a) + abs(q - b) + max(0, r - c)


N = int(input())
xyz = [tuple(map(int, input().split())) for _ in range(N)]

g = defaultdict(list)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a, b, c = xyz[i]
        p, q, r = xyz[j]
        cost = calc(a, b, c, p, q, r)
        g[i].append((cost, j))


INF = float('inf')
dp = [[INF] * (1 << N) for _ in range(N)]
for nc, nv in g[0]:
    dp[nv][1 << nv] = nc

for now in range(1 << N):
    for v in range(N):
        if not now >> v & 1:
            continue
        for nc, nv in g[v]:
            if now >> nv & 1:
                continue
            nxt = now | 1 << nv
            dp[nv][nxt] = min(dp[nv][nxt], dp[v][now] + nc)
print(dp[0][-1])
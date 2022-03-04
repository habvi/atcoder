n, m = map(int, input().split())

INF = float('inf')
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    dist[a][b] = c

ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d = min(dist[i][j], dist[i][k] + dist[k][j])
            dist[i][j] = d
            if d != INF:
                ans += d
print(ans)
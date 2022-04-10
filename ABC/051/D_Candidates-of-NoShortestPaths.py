n, m = map(int, input().split())

INF = float('inf')
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    dist[a][b] = c
    dist[b][a] = c
    edge.append((a, b, c))

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for a, b, c in edge:
    ans += (dist[a][b] < c)

print(ans)
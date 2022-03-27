from collections import defaultdict
from itertools import combinations

n, m = map(int, input().split())

INF = float('inf')
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    if a == 0 or b == 0:
        g[a].append((b, c))
        g[b].append((a, c))
        continue
    dist[a][b] = c
    dist[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = INF
for (v1, c1), (v2, c2) in combinations(g[0], 2):
    total = c1 + c2 + dist[v1][v2]
    ans = min(ans, total)

print(ans if ans != INF else -1)
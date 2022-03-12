from collections import defaultdict

n, m = map(int, input().split())

edges = defaultdict(int)
INF = float('inf')
dst = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[(a, b)] = c
    dst[a][b] = c
    dst[b][a] = c

for i in range(n):
    dst[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j])

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        cost = edges[(i, j)]
        if not cost:
            continue

        for k in range(n):
            if k not in (i, j) and dst[i][k] + dst[k][j] <= cost:
                ans += 1
                break
print(ans)
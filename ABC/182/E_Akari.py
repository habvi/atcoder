h, w, n, m = map(int, input().split())

# light : 1, block : -1
g = [[0] * w for _ in range(h)]
for _ in range(n):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a][b] = 1

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a][b] = -1

row = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if g[i][j] <= 0 or row[i][j]:
            continue

        y, x = i, j
        while x >= 0 and g[y][x] != -1:
            row[y][x] = 1
            x -= 1
        y, x = i, j
        while x < w and g[y][x] != -1:
            row[y][x] = 1
            x += 1

col = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if g[i][j] <= 0 or col[i][j]:
            continue

        y, x = i, j
        while y >= 0 and g[y][x] != -1:
            col[y][x] = 1
            y -= 1
        y, x = i, j
        while y < h and g[y][x] != -1:
            col[y][x] = 1
            y += 1

ans = 0
for i in range(h):
    for j in range(w):
        ans += (row[i][j] | col[i][j])
print(ans)
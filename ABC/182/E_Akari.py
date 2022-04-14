h, w, n, m = map(int, input().split())
S = [[0] * w for _ in range(h)]

seen = [[0] * w for _ in range(h)]
light = []
for _ in range(n):
    a, b = map(lambda x: int(x) - 1, input().split())
    S[a][b] = 1
    light.append((a, b))

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    S[a][b] = '#'

row = [[0] * w for _ in range(h)]
for a, b in light:
    if row[a][b]:
        continue
    row[a][b] = 1

    y, x = a, b
    while y - 1 >= 0 and S[y - 1][x] != '#':
        row[y - 1][x] = 1
        y -= 1
    y, x = a, b
    while y + 1 < h and S[y + 1][x] != '#':
        row[y + 1][x] = 1
        y += 1

col = [[0] * w for _ in range(h)]
for a, b in light:
    if col[a][b]:
        continue
    col[a][b] = 1

    y, x = a, b
    while x - 1 >= 0 and S[y][x - 1] != '#':
        col[y][x - 1] = 1
        x -= 1
    y, x = a, b
    while x + 1 < w and S[y][x + 1] != '#':
        col[y][x + 1] = 1
        x += 1

ans = 0
for i in range(h):
    for j in range(w):
        ans += (row[i][j] or col[i][j])
print(ans)
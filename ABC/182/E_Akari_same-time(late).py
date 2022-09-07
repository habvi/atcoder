H, W, N, M = map(int, input().split())

# light : 1, block : -1
g = [[0] * W for _ in range(H)]
for _ in range(N):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a][b] = 1
for _ in range(M):
    c, d = map(lambda x: int(x) - 1, input().split())
    g[c][d] = -1

# row, col
light = [[[0, 0] for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if g[i][j] <= 0:
            continue

        if not light[i][j][0]:
            y, x = i, j
            while x >= 0 and g[y][x] != -1:
                light[y][x][0] = 1
                x -= 1
            y, x = i, j
            while x < W and g[y][x] != -1:
                light[y][x][0] = 1
                x += 1

        if not light[i][j][1]:
            y, x = i, j
            while y >= 0 and g[y][x] != -1:
                light[y][x][1] = 1
                y -= 1
            y, x = i, j
            while y < H and g[y][x] != -1:
                light[y][x][1] = 1
                y += 1

ans = 0
for i in range(H):
    for j in range(W):
        ans += (sum(light[i][j]) >= 1)
print(ans)
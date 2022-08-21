H, W = map(int, input().split())
G = [input() for _ in range(H)]

dir = "RDLU"
DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]
seen = [[0] * W for _ in range(H)]
seen[0][0] = 1
y, x = 0, 0
while True:
    nxt = G[y][x]
    i = dir.index(nxt)
    dy, dx = DXY[i]
    ny, nx = y + dy, x + dx
    if not (0 <= ny < H and 0 <= nx < W):
        print(y + 1, x + 1)
        exit()
    if seen[ny][nx]:
        print(-1)
        exit()
    seen[ny][nx] = 1
    y, x = ny, nx
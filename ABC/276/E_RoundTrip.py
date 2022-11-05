from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(que):
    while que:
        y, x = que.popleft()
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < H and 0 <= nx < W) or C[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))


H, W = map(int, input().split())
C = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if C[i][j] == 'S':
            sy, sx = i, j
            break
    else:
        continue
    break

for dy, dx in DXY:
    ny, nx = sy + dy, sx + dx
    if not (0 <= ny < H and 0 <= nx < W) or C[ny][nx] == '#':
        continue
    dist = [[-1] * W for _ in range(H)]
    dist[sy][sx] = 0
    dist[ny][nx] = 1
    que = deque([])
    que.append((ny, nx))
    bfs(que)

    around = set()
    for dy, dx in DXY:
        ny, nx = sy + dy, sx + dx
        if not (0 <= ny < H and 0 <= nx < W) or C[ny][nx] == '#':
            continue
        if dist[ny][nx] != -1:
            around.add(dist[ny][nx])
        if len(around) >= 2:
            print("Yes")
            exit()
print("No")

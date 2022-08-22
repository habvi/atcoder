from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    dist = [[-1] * W for _ in range(H)]
    dist[sy][sx] = 1
    que = deque([])
    que.append((sy, sx))
    while que:
        y, x = que.popleft()
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < H and 0 <= nx < W) or S[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))
    return dist


H, W = map(int, input().split())
S = [input() for _ in range(H)]

dist = bfs(0, 0)
if dist[-1][-1] == -1:
    print(-1)
    exit()

black = 0
for s in S:
    black += s.count('#')
print(H * W - black - dist[-1][-1])
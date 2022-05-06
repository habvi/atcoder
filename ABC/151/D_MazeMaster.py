from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    global ans
    dist = [[-1] * w for _ in range(h)]
    dist[sy][sx] = 0
    que = deque([])
    que.append((sy, sx))
    while que:
        y, x = que.popleft()
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or S[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[y][x] + 1
            ans = max(ans, dist[ny][nx])
            que.append((ny, nx))


h, w = map(int, input().split())
S = [input() for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            continue
        bfs(i, j)
print(ans)
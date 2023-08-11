from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    dist = [[-1] * M for _ in range(N)]
    dist[sy][sx] = 0
    que = deque([])
    que.append((sy, sx))
    while que:
        y, x = que.popleft()
        for dy, dx in DXY:
            ny, nx = y, x
            while True:
                if S[ny + dy][nx + dx] == '#':
                    if (ny, nx) != (y, x):
                        if dist[ny][nx] == -1:
                            dist[ny][nx] = dist[y][x] + 1
                            que.append((ny, nx))
                    break
                dist[ny][nx] = dist[y][x] + 1
                ny, nx = ny + dy, nx + dx
    return dist


N, M = map(int, input().split())
S = [input() for _ in range(N)]

dist = bfs(1, 1)
ans = 0
for d in dist:
    ans += M - d.count(-1)
print(ans)

from collections import deque

DXY = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def bfs(sy, sx):
    for dir in range(2):
        dist[dir][sy][sx] = 0

    que = deque([])
    for dir, (dy, dx) in enumerate(DXY):
        ny, nx = sy + dy, sx + dx
        if not (0 <= ny < n and 0 <= nx < n) or S[ny][nx] == '#':
            continue
        dir = dir % 2
        dist[dir][ny][nx] = 1
        que.append((ny, nx, dir, 1))

    while que:
        y, x, dir, c = que.popleft()
        if (y, x) == (gy, gx):
            print(dist[dir][y][x])
            exit()

        nc = dist[dir][y][x]
        if c > nc:
            continue

        for ndir, (dy, dx) in enumerate(DXY):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n) or S[ny][nx] == '#':
                continue

            ndir = ndir % 2
            if dir == ndir:
                if dist[ndir][ny][nx] <= nc:
                    continue
                dist[ndir][ny][nx] = nc
                que.appendleft((ny, nx, ndir, nc))
            else:
                if dist[ndir][ny][nx] <= nc + 1:
                    continue
                dist[ndir][ny][nx] = nc + 1
                que.append((ny, nx, ndir, nc + 1))
 


n = int(input())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())
S = [input() for _ in range(n)]

INF = float('inf')
dist = [[[INF] * n for _ in range(n)] for _ in range(2)]
bfs(sy, sx)

print(-1)
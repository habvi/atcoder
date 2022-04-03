from collections import deque

XY = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def bfs(sy, sx):
    for dir in range(2):
        dist[sy][sx][dir] = 0

    que = deque([])
    for dir, (dy, dx) in enumerate(XY):
        ny, nx = sy + dy, sx + dx
        if not (0 <= ny < n and 0 <= nx < n) or S[ny][nx] == '#':
            continue
        dist[ny][nx][dir % 2] = 1
        que.append((ny, nx, dir % 2))

    while que:
        y, x, dir = que.popleft()
        if (y, x) == (gy, gx):
            return

        d = dist[y][x][dir]
        for ndir, (dy, dx) in enumerate(XY):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n) or S[ny][nx] == '#':
                continue

            ndir = ndir % 2
            if dir == ndir:
                if dist[ny][nx][ndir] <= d:
                    continue
                dist[ny][nx][ndir] = d
                que.appendleft((ny, nx, ndir))
            else:
                if dist[ny][nx][ndir] <= d + 1:
                    continue
                dist[ny][nx][ndir] = d + 1
                que.append((ny, nx, ndir))
 


n = int(input())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())
S = [input() for _ in range(n)]

INF = float('inf')
dist = [[[INF] * 2 for _ in range(n)] for _ in range(n)]
bfs(sy, sx)

ans = min(dist[gy][gx])
print(ans if ans != INF else -1)
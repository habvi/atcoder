from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    dist[sy][sx] = 0
    que = deque([])
    que.append((sy, sx, 0))

    while que:
        y, x, c = que.popleft()
        if (y, x) == (h - 1, w - 1):
            print(dist[h - 1][w - 1])
            exit()

        nc = dist[y][x]
        if c > nc:
            continue

        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or S[ny][nx] == '#':
                continue
            if dist[ny][nx] <= nc:
                continue
            dist[ny][nx] = nc
            que.appendleft((ny, nx, nc))

        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if abs(dy) + abs(dx) == 4 or (dy, dx) == (0, 0):
                    continue
                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < w):
                    continue
                if dist[ny][nx] <= nc + 1:
                    continue
                dist[ny][nx] = nc + 1
                que.append((ny, nx, nc + 1))


h, w = map(int, input().split())
S = [input() for _ in range(h)]

INF = float('inf')
dist = [[INF] * w for _ in range(h)]
bfs(0, 0)
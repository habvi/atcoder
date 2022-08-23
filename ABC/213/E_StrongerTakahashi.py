from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    INF = float('inf')
    dist = [[INF] * W for _ in range(H)]
    dist[sy][sx] = 0
    que = deque([])
    que.append((sy, sx, 0))
    while que:
        y, x, c = que.popleft()
        if (y, x) == (H - 1, W - 1):
            return dist[-1][-1]

        nc = dist[y][x]
        if nc < c:
            continue
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < H and 0 <= nx < W) or S[ny][nx] == '#':
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
                if not (0 <= ny < H and 0 <= nx < W):
                    continue
                if dist[ny][nx] <= nc + 1:
                    continue
                dist[ny][nx] = nc + 1
                que.append((ny, nx, nc + 1))
    return dist[-1][-1]


H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = bfs(0, 0)
print(ans)
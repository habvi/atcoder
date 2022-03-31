from collections import deque

def bfs(sy, sx):
    dist[sy][sx] = 0
    q = deque([])
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        d = dist[y][x]
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or S[ny][nx] == '#':
                continue
            if dist[ny][nx] <= d:
                continue
            dist[ny][nx] = d
            q.appendleft((ny, nx))

        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if abs(dy) + abs(dx) == 4 or (dy, dx) == (0, 0):
                    continue
                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < w):
                    continue
                if dist[ny][nx] <= d + 1:
                    continue
                dist[ny][nx] = d + 1
                q.append((ny, nx))


h, w = map(int, input().split())
S = [input() for _ in range(h)]

INF = float('inf')
dist = [[INF] * w for _ in range(h)]
bfs(0, 0)

print(dist[h - 1][w - 1])
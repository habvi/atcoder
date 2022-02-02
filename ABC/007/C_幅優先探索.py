from collections import deque

def bfs(sy, sx):
    dst = [[-1] * w for _ in range(h)]
    dst[sy][sx] = 0
    q = deque([])
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or g[ny][nx] == '#':
                continue
            if dst[ny][nx] != -1:
                continue
            dst[ny][nx] = dst[y][x] + 1
            q.append((ny, nx))
    return dst


h, w = map(int, input().split())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())
g = [input() for _ in range(h)]

dst = bfs(sy, sx)
print(dst[gy][gx])
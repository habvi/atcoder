from collections import deque
def bfs(sy, sx):
    dst[sy][sx] = 0
    q = deque([])
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        if seen[y][x]:
            continue
        seen[y][x] = 1

        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or s[ny][nx] == "#":
                continue
            if dst[ny][nx] <= dst[y][x]:
                continue
            dst[ny][nx] = dst[y][x] 
            q.appendleft((ny, nx))

        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if dy == dx == 0:
                    continue
                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < w) or s[ny][nx] == "#":
                    continue
                if dst[ny][nx] <= dst[y][x] + 1:
                    continue
                dst[ny][nx] = dst[y][x] + 1
                q.append((ny, nx))

h, w = map(int, input().split())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())
s = [input() for _ in range(h)]
dst = [[float('inf')] * w for _ in range(h)]
seen = [[0] * w for _ in range(h)]
bfs(sy, sx)
print(dst[gy][gx] if dst[gy][gx] != float('inf') else -1)
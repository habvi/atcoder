from collections import deque
def bfs(sy, sx):
    dst[sy][sx] = 0
    q = deque([])
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        if seen[y][x]: continue
        seen[y][x] = 1
        d = dst[y][x]
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w): continue
            if s[ny][nx] == "#": continue
            if dst[ny][nx] <= d: continue
            dst[ny][nx] = d 
            q.appendleft((ny, nx))
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if dy == dx == 0: continue
                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < w): continue
                if s[ny][nx] == "#": continue
                if dst[ny][nx] <= d + 1: continue
                dst[ny][nx] = d + 1
                q.append((ny, nx))

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch -= 1; cw -= 1; dh -= 1; dw -= 1
s = [input() for _ in range(h)]
dst = [[float('inf')] * w for _ in range(h)]
seen = [[0] * w for _ in range(h)]
bfs(ch, cw)
print(dst[dh][dw] if dst[dh][dw] != float('inf') else -1)
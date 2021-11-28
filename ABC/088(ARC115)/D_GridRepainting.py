from collections import deque
def bfs(sy, sx):
    dst[sy][sx] = 0
    que = deque([])
    que.append([sy, sx])
    while que:
        y, x = que.popleft()
        for dy, dx in zip([0,1,0,-1], [1,0,-1,0]):
            ny, nx = y+dy, x+dx
            if (not 0 <= ny < h) or (not 0 <= nx < w): continue
            if s[ny][nx] == '#': continue
            if dst[ny][nx] != -1: continue
            dst[ny][nx] = dst[y][x] + 1
            que.append([ny, nx])

h, w = map(int, input().split())
s = [input() for _ in range(h)]
dst = [[-1]*w for _ in range(h)]
bfs(0, 0)

if dst[h - 1][w - 1] == -1:
    print(-1)
    exit()

bl = 0
for b in s:
    bl += b.count('#')
print(h * w - bl - dst[h - 1][w - 1] - 1)
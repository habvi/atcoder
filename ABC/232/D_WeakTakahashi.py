import sys
sys.setrecursionlimit(10 ** 7)
def dfs(y, x, d):
    dst[y][x] = d
    mx[0] = max(mx[0], d)
    for dy, dx in zip((0, 1), (1, 0)):
        ny, nx = y + dy, x + dx
        if (not 0 <= ny < h) or (not 0 <= nx < w): continue
        if c[ny][nx] == '#': continue
        if dst[ny][nx] != -1: continue
        dfs(ny, nx, d + 1)

h, w = map(int, input().split())
c = [input() for _ in range(h)]
dst = [[-1] * w for _ in range(h)]
mx = [0]
dfs(0, 0, 1)
print(mx[0])
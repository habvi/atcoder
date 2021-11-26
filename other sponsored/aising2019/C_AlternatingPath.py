import sys
sys.setrecursionlimit(10 ** 7)
def dfs(y, x):
    seen[y][x] = 1
    if s[y][x] == "#": bl[0] += 1
    else: wh[0] += 1
    for dy, dx in zip((-1, 0, 1, 0), (0, 1, 0, -1)):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < h and 0 <= nx < w): continue
        if seen[ny][nx]: continue
        if s[ny][nx] == s[y][x]: continue
        dfs(ny, nx)

h, w = map(int, input().split())
s = [input() for _ in range(h)]
bw = [[-1] * w for _ in range(h)]
seen = [[0] * w for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if seen[i][j]: continue
        bl, wh = [0], [0]
        dfs(i, j)
        ans += bl[0] * wh[0]
print(ans)
import sys
sys.setrecursionlimit(10**7)
def dfs(y, x):
    seen[y][x] = 1
    for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
        ny, nx = y + dy, x + dx
        if (not 0 <= ny < h) or (not 0 <= nx < w): continue
        if g[ny][nx] == 'x': continue
        if seen[ny][nx]: continue
        dfs(ny, nx)

h, w = 10, 10
g = [list(input()) for _ in range(h)]
cnt = 0
for gg in g:
    cnt += gg.count('o')

for i in range(h):
    for j in range(w):
        if g[i][j] == 'x':
            g[i][j] = 'o'
            seen = [[0] * w for _ in range(h)]
            dfs(i, j)

            tot = sum([sum(s) for s in seen])
            if tot == cnt + 1:
                print('YES')
                exit()
            g[i][j] = 'x'
print('NO')
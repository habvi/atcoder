import sys
sys.setrecursionlimit(10 ** 7)

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(y, x):
    global black, white
    seen[y][x] = 1
    for dy, dx in DXY:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < h and 0 <= nx < w) or seen[ny][nx]:
            continue
        if S[y][x] == S[ny][nx]:
            continue
        black += (S[ny][nx] == '#')
        white += (S[ny][nx] == '.')
        dfs(ny, nx)


h, w = map(int, input().split())
S = [input() for _ in range(h)]

ans = 0
seen = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if not seen[i][j] and S[i][j] == '#':
            black, white = 1, 0
            dfs(i, j)
            ans += black * white
print(ans)
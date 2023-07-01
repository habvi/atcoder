import sys
sys.setrecursionlimit(10 ** 7)

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(y, x, dist):
    seen[y][x] = 1
    if y == H - 1 and x == W - 1:
        print("Yes")
        exit()
    for dy, dx in DXY:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        n_dist = (dist + 1) % 5
        if S[ny][nx] != SNUKE[n_dist]:
            continue
        if seen[ny][nx]:
            continue
        dfs(ny, nx, n_dist)

H, W = map(int, input().split())
S = [input() for _ in range(H)]
SNUKE = "snuke"

if S[0][0] != 's':
    print("No")
    exit()

seen = [[0] * W for _ in range(H)]
dfs(0, 0, 0)
print("No")
import sys
sys.setrecursionlimit(10**7)
def dfs(y, x):
    seen[y][x] = 1
    for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < h and 0 <= nx < w) or seen[ny][nx]:
            continue
        dfs(ny, nx)
        if a[ny][nx] % 2 == 1:
            a[y][x] += 1
            a[ny][nx] -= 1
            ans.append((ny + 1, nx + 1, y + 1, x + 1))

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
seen = [[0] * w for _ in range(h)]
ans = []
dfs(0, 0)

print(len(ans))
for a in ans:
    print(*a)
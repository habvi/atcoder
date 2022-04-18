from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    que = deque([])
    que.append((sy, sx))
    while que:
        y, x = que.popleft()
        seen[y][x] = 1
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n + 2 and 0 <= nx < n + 2) or seen[ny][nx]:
                continue
            que.append((ny, nx))

def new(x):
    return divmod(x, n)

def field(seen):
    return sum(sum(g) for g in seen)


n = 4
A = [tuple(map(int, input().split())) for _ in range(n)]
m = n * n

total_v = sum(sum(a) for a in A)

ans = 0
for bit in range(1, 1 << m):
    village = 0
    inside = None
    g_in = [[1] * (n + 2) for _ in range(n + 2)]
    g_out = [[0] * (n + 2) for _ in range(n + 2)]
    for now in range(m):
        if bit >> now & 1:
            inside = now
            i, j = new(now)
            village += A[i][j]
            g_in[i + 1][j + 1] = 0
            g_out[i + 1][j + 1] = 1

    if village != total_v:
        continue

    seen = [g[:] for g in g_in]
    i, j = new(inside)
    bfs(i + 1, j + 1)
    ok_in = (field(seen) == (n + 2)**2)

    seen = [g[:] for g in g_out]
    bfs(0, 0)
    ok_out = (field(seen) == (n + 2)**2)

    ans += (ok_in and ok_out)
print(ans)
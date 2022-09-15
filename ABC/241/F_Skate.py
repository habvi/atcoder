from bisect import bisect, bisect_left
from collections import defaultdict, deque

def bfs(sy, sx):
    def check(ny, nx):
        if dist[(ny, nx)] != -1:
            return True
        dist[(ny, nx)] = dist[(y, x)] + 1
        if (ny, nx) == (gy, gx):
            return False
        que.append((ny, nx))
        return True

    que = deque([])
    que.append((sy, sx))
    dist = defaultdict(lambda : -1)
    dist[(sy, sx)] = 0
    while que:
        y, x = que.popleft()
        l = bisect_left(row[y], x)
        if l != 0:
            nx = row[y][l - 1]
            if x - 1 != nx:
                if not check(y, nx + 1):
                    return dist
        r = bisect(row[y], x)
        if r != len(row[y]):
            nx = row[y][r]
            if x + 1 != nx:
                if not check(y, nx - 1):
                    return dist
        u = bisect_left(col[x], y)
        if u != 0:
            ny = col[x][u - 1]
            if y - 1 != ny:
                if not check(ny + 1, x):
                    return dist
        d = bisect(col[x], y)
        if d != len(col[x]):
            ny = col[x][d]
            if y + 1 != ny:
                if not check(ny - 1, x):
                    return dist
    return dist


H, W, N = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

row = defaultdict(set)
col = defaultdict(set)
for _ in range(N):
    y, x = map(int, input().split())
    row[y].add(x)
    col[x].add(y)
for k in row.keys():
    row[k] = sorted(row[k])
for k in col.keys():
    col[k] = sorted(col[k])

dist = bfs(sy, sx)
print(dist[(gy, gx)])
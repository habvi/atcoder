from collections import defaultdict
from collections import deque
def bfs(sy, sx):
    dst[sy][sx] = 0
    q = deque([(sy, sx)])
    used = set()
    while q:
        y, x = q.popleft()
        if (y, x) == (gy, gx):
            return

        d = dst[y][x]
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if a[ny][nx] == '#':
                continue
            if dst[ny][nx] == -1:
                dst[ny][nx] = d + 1
                q.append((ny, nx))
        
        al = a[y][x]
        if al in 'SG.#' or al in used:
            continue
        used.add(al)
        for ny, nx in p[al]:
            if (ny, nx) == (y, x):
                continue
            if dst[ny][nx] == -1:
                dst[ny][nx] = d + 1
                q.append((ny, nx))

h, w = map(int, input().split())
a = [input() for _ in range(h)]
p = defaultdict(list)
for i in range(h):
    for j in range(w):
        b = a[i][j]
        if b == 'S':
            sy, sx = i, j
        elif b == 'G':
            gy, gx = i, j
        elif b.islower():
            p[b].append((i, j))

dst = [[-1] * w for _ in range(h)]
bfs(sy, sx)
print(dst[gy][gx])
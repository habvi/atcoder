from collections import defaultdict, deque

def bfs(sy, sx):
    dist[sy][sx] = 0
    que = deque([(sy, sx)])
    used = set()
    while que:
        y, x = que.popleft()
        if (y, x) == (gy, gx):
            return

        d = dist[y][x]
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or A[ny][nx] == '#':
                continue
            if dist[ny][nx] == -1:
                dist[ny][nx] = d + 1
                que.append((ny, nx))

        a = A[y][x]
        if a == '.' or a in used:
            continue
        used.add(a)

        for ny, nx in alph[a]:
            if (ny, nx) == (y, x):
                continue
            if dist[ny][nx] == -1:
                dist[ny][nx] = d + 1
                que.append((ny, nx))


h, w = map(int, input().split())
A = [input() for _ in range(h)]

alph = defaultdict(list)
for i in range(h):
    for j in range(w):
        a = A[i][j]
        if a == 'S':
            sy, sx = i, j
        elif a == 'G':
            gy, gx = i, j
        elif a.islower():
            alph[a].append((i, j))

dist = [[-1] * w for _ in range(h)]
bfs(sy, sx)

print(dist[gy][gx])
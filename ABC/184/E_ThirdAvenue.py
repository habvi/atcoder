from collections import defaultdict, deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    dist = [[-1] * W for _ in range(H)]
    dist[sy][sx] = 0
    que = deque([])
    que.append((sy, sx))
    used = set()
    while que:
        y, x = que.popleft()
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < H and 0 <= nx < W) or S[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))

        nxt = S[y][x]
        if nxt not in "SG.":
            if nxt in used:
                continue
            for ny, nx in alph[nxt]:
                if dist[ny][nx] != -1:
                    continue
                dist[ny][nx] = dist[y][x] + 1
                que.append((ny, nx))
            used.add(nxt)
    return dist


H, W = map(int, input().split())
S = [input() for _ in range(H)]

alph = defaultdict(list)
for i in range(H):
    for j in range(W):
        a = S[i][j]
        if a == 'S':
            sy, sx = i, j
        elif a == 'G':
            gy, gx = i, j
        elif a != '.':
            alph[a].append((i, j))
dist = bfs(sy, sx)
print(dist[gy][gx])
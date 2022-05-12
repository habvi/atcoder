from collections import deque

DXY = [(0, 1), (1, 0)]

def bfs(sy, sx):
    dist = [[-1] * w for _ in range(h)]
    dist[sy][sx] = 1
    que = deque([])
    que.append((sy, sx))
    while que:
        y, x = que.popleft()
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or S[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))
    return dist


h, w = map(int, input().split())
S = [input() for _ in range(h)]

dist = bfs(0, 0)
ans = max(max(d) for d in dist)
print(ans)
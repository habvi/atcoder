from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    dist = [[INF] * w for _ in range(h)]
    dist[sy][sx] = 0
    que = deque([])
    que.append((sy, sx))

    while que:
        y, x = que.popleft()
        d = dist[y][x] + 1
        for dy, dx in DXY:
            for i in range(1, K + 1):
                ny = y + dy * i
                nx = x + dx * i
                if (0 <= ny < h and 0 <= nx < w) and S[ny][nx] != '@':
                    nd = dist[ny][nx]
                    if d > nd:
                        break
                    if d < nd:
                        dist[ny][nx] = d
                        que.append((ny, nx))
                else:
                    break
    return dist


h, w, K = map(int, input().split())
sy, sx, gy, gx = map(lambda x: int(x) - 1, input().split())
S = [input() for _ in range(h)]

INF = float('inf')
dist = bfs(sy, sx)

ans = dist[gy][gx]
print(ans if ans != INF else -1)
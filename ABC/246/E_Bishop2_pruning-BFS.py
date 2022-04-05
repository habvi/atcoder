from collections import deque

DXY = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(sy, sx):
    dist = [[INF] * w for _ in range(h)]
    dist[sy][sx] = 0
    que = deque([])
    que.append((sy, sx))

    while que:
        y, x = que.popleft()
        d = dist[y][x] + 1
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx

            while (0 <= ny < h and 0 <= nx < w) and S[ny][nx] != '#':
                nd = dist[ny][nx]
                if d > nd:
                    break
                if d < nd:
                    dist[ny][nx] = d
                    que.append((ny, nx))
                ny, nx = ny + dy, nx + dx

    return dist


n = int(input())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())
h, w = n, n
S = [input() for _ in range(h)]

INF = float('inf')
dist = bfs(sy, sx)

ans = dist[gy][gx]
print(ans if ans != INF else -1)
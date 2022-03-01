from collections import deque

def bfs(sy, sx):
    global ans
    dist[sy][sx] = 0
    q = deque([])
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < r and 0 <= nx < c):
                continue
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[y][x] + 1
            nd = dist[ny][nx]
            if nd <= d and nd % 2 == d % 2:
                ans = max(ans, g[ny][nx])
            q.append((ny, nx))


r, c, d = map(int, input().split())
g = [tuple(map(int, input().split())) for _ in range(r)]

dist = [[-1] * c for _ in range(r)]
ans = 0 if d % 2 else g[0][0]
bfs(0, 0)

print(ans)
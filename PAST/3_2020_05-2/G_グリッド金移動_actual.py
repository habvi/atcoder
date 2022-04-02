from collections import deque
n, gx, gy = map(int, input().split())
gx, gy = gx+203, gy+203
sx, sy = 203, 203

a = [['.']*410 for _ in range(410)]
for i in range(n):
    x, y = map(int, input().split())
    x, y = x+203, y+203
    a[y][x] = '#'

dst = [[-1]*410 for _ in range(410)]
dst[sy][sx] = 0
que = deque([])
que.append([sy, sx])

while que:
    y, x = que.popleft()
    dx = [1, 0, -1, 1, -1, 0]
    dy = [1, 1, 1, 0, 0, -1]
    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        if ny < 0 or ny >= 410 or nx < 0 or nx >= 410:
            continue
        if a[ny][nx] == '#':
            continue
        if dst[ny][nx] != -1:
            continue

        dst[ny][nx] = dst[y][x] + 1
        if nx == gx and ny == gy:
            print(dst[ny][nx])
            exit()

        que.append([ny, nx])
print(-1)

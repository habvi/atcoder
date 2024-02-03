from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(y1, x1, y2, x2):
    dist = [[[[-1] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    dist[y1][x1][y2][x2] = 0
    que = deque([])
    que.append((y1, x1, y2, x2))
    while que:
        y1, x1, y2, x2 = que.popleft()
        for dy, dx in DXY:
            def calc_next(y, x):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < N and 0 <= nx < N) or S[ny][nx] == '#':
                    return y, x
                else:
                    return ny, nx

            ny1, nx1 = calc_next(y1, x1)
            ny2, nx2 = calc_next(y2, x2)
            if dist[ny1][nx1][ny2][nx2] != -1:
                continue

            dist[ny1][nx1][ny2][nx2] = dist[y1][x1][y2][x2] + 1
            if (ny1, nx1) == (ny2, nx2):
                return dist[ny1][nx1][ny2][nx2]
            que.append((ny1, nx1, ny2, nx2))
    return -1


N = int(input())
S = [input() for _ in range(N)]

p = []
for i in range(N):
    for j in range(N):
        if S[i][j] == 'P':
            p.append(i)
            p.append(j)
print(bfs(*p))
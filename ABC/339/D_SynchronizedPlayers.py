from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(ay, ax, by, bx):
    dist = [[[[-1] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    dist[ay][ax][by][bx] = 0
    que = deque([])
    que.append((ay, ax, by, bx))
    while que:
        y1, x1, y2, x2 = que.popleft()
        for dy, dx in DXY:
            ny1, nx1 = y1 + dy, x1 + dx
            if not (0 <= ny1 < N and 0 <= nx1 < N) or S[ny1][nx1] == '#':
                ny1, nx1 = y1, x1
            ny2, nx2 = y2 + dy, x2 + dx
            if not (0 <= ny2 < N and 0 <= nx2 < N) or S[ny2][nx2] == '#':
                ny2, nx2 = y2, x2
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
from collections import deque

# 右下左上
DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    dist = [[-1] * W for _ in range(H)]
    que = deque([])
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'E':
                dist[i][j] = 0
                que.append((i, j))
    while que:
        y, x = que.popleft()
        for i, (dy, dx) in enumerate(DXY):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < H and 0 <= nx < W) or S[ny][nx] == '#':
                continue
            if dist[ny][nx] != -1:
                continue
            if i == 0:
                S[ny][nx] = '<'
            elif i == 1:
                S[ny][nx] = '^'
            elif i == 2:
                S[ny][nx] = '>'
            else:
                S[ny][nx] = 'v'
            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))
    return dist


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

bfs()
for s in S:
    print("".join(s))

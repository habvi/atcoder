from collections import deque

def bfs(sy, sx):
    g[sy][sx] = 1
    que = deque([])
    que.append((sy, sx))
    while que:
        y, x = que.popleft()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == dx == 0 or S[1 + dy][1 + dx] == '.':
                    continue

                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < w) or g[ny][nx]:
                    continue

                g[ny][nx] = 1
                que.append((ny, nx))


A, B = map(lambda x: int(x) - 1, input().split())
S = [input() for _ in range(3)]
h, w = 9, 9

g = [[0] * w for _ in range(h)]
bfs(A, B)

ans = sum(sum(gl) for gl in g)
print(ans)
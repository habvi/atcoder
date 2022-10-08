N, M = map(int, input().split())

num = [i * i for i in range(N + 1)]
d = []
for i in range(len(num)):
    for j in range(len(num)):
        if num[i] + num[j] == M:
            d.append((i, j))

DXY = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
dst = [[-1] * N for _ in range(N)]
dst[0][0] = 0
pre = [(0, 0)]
while pre:
    nxt = []
    for y, x in pre:
        for oy, ox in d:
            for dy, dx in DXY:
                ny, nx = y + dy * oy, x + dx * ox
                if not (0 <= ny < N and 0 <= nx < N) or dst[ny][nx] != -1:
                    continue
                dst[ny][nx] = dst[y][x] + 1
                nxt.append((ny, nx))
    pre = nxt

for a in dst:
    print(*a)
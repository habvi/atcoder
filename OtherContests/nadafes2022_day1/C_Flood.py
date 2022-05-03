from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(sy, sx):
    global t
    human = deque()
    human.append((sy, sx))
    while human:
        if t > 0 and t % K == 0:
            for _ in range(len(magma)):
                my, mx = magma.popleft()
                for dy, dx in DXY:
                    nmy, nmx = my + dy, mx + dx
                    if not (0 <= nmy < h and 0 <= nmx < w) or A[nmy][nmx] != '.':
                        continue
                    A[nmy][nmx] = '@'
                    magma.append((nmy, nmx))

        for _ in range(len(human)):
            y, x = human.popleft()
            if A[y][x] != '.':
                continue

            for dy, dx in DXY:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < w) or A[ny][nx] != '.':
                    continue
                human.append((ny, nx))
            A[y][x] = '#'

        t += 1


h, w, K = map(int, input().split())
A = [list(input()) for _ in range(h)]

magma = deque()
for y in range(h):
    for x in range(w):
        if A[y][x] == '@':
            magma.append((y, x))

t = 0
bfs(0, 0)

print('Yes' if A[-1][-1] == '#' else 'No')
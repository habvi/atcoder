h, w = map(int, input().split())
S = [input() for _ in range(h)]

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for y in range(h):
    for x in range(w):
        if S[y][x] == '.':
            continue

        num = 0
        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            num += (S[ny][nx] == '#')

        if not num:
            print('No')
            exit()

print('Yes')
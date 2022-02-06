h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if g[i][j] != '.': continue

        used = set()
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = i + dy, j + dx
            if not (0 <= ny < h and 0 <= nx < w) or g[ny][nx] == '.':
                continue
            used.add(g[ny][nx])

        for k in range(1, 6):
            if str(k) not in used:
                g[i][j] = str(k)
                break

for ans in g:
    print(''.join(ans))
h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if g[i][j] != '.': continue
        s = set()
        for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            ny, nx = i + dy, j + dx
            if not (0 <= ny < h and 0 <= nx < w): continue
            if g[ny][nx] == '.': continue
            s.add(g[ny][nx])

        for c in ('1', '2', '3', '4', '5'):
            if c in s:
                continue
            g[i][j] = c
            break

for gg in g:
    print(''.join(gg))
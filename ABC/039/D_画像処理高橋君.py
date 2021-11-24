h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
seen = [["."] * w for _ in range(h)]
ans = [["."] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '.': continue
        tot, shp = 0, 0
        p = [(i, j)]
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == dx == 0: continue
                y, x = i + dy, j + dx
                if not (0 <= y < h and 0 <= x < w): continue
                tot += 1
                if s[y][x] == '.': continue
                shp += 1
                p.append((y, x))
        if tot == shp:
            ans[i][j] = "#"
            for y, x in p:
                seen[y][x] = "#"

if s == seen:
    print('possible')
    for a in ans:
        print("".join(a))
else:
    print('impossible')

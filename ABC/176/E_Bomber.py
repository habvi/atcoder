h, w, m = map(int, input().split())
g = set()
row = [0] * h
col = [0] * w
for _ in range(m):
    y, x = map(int, input().split())
    y -= 1; x -= 1
    row[y] += 1
    col[x] += 1
    g.add((y, x))

mr, mc = max(row), max(col)
ri, ci = [], []
for i, r in enumerate(row):
    if r == mr:
        ri.append(i)
for i, c in enumerate(col):
    if c == mc:
        ci.append(i)

ans = mr + mc
for r in ri:
    for c in ci:
        if (r, c) in g:
            continue
        print(ans)
        exit()
ans -= 1
print(ans)
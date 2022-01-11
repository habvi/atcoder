h, w, m = map(int, input().split())
bomb = set()
row = [0] * h
col = [0] * w
for _ in range(m):
    y, x = map(lambda x: int(x) - 1, input().split())
    bomb.add((y, x))
    row[y] += 1
    col[x] += 1

mxr = max(row)
ri = [i for i, r in enumerate(row) if r == mxr]

mxc = max(col)
ci = [i for i, c in enumerate(col) if c == mxc]

ans = mxr + mxc
for i in ri:
    for j in ci:
        if (i, j) not in bomb:
            print(ans)
            exit()
print(ans - 1)
h, w, k = map(int, input().split())
S = [input() for _ in range(h)]

g = [[None] * w for _ in range(h)]
num = 1
for i in range(h):
    if '#' not in S[i]:
        continue

    ignore = True
    for j in range(w):
        if S[i][j] == '#' and ignore:
            g[i][j] = num
            ignore = False
            continue
        if S[i][j] == '#':
            num += 1
        g[i][j] = num
    num += 1

for i in range(h):
    for j in range(w):
        if g[i][j]:
            num = g[i][j]
            up = i
            while up - 1 >= 0 and g[up - 1][j] is None:
                up -= 1
                g[up][j] = num

            down = i
            while down + 1 < h and g[down + 1][j] is None:
                down += 1
                g[down][j] = num

for ans in g:
    print(*ans)
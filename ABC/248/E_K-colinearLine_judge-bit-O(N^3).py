from collections import defaultdict

def is_point_on_line(x1, y1, x2, y2, px, py):
    return (x2 - x1)*(py - y1) == (y2 - y1)*(px - x1)


n, K = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]

if K == 1:
    print('Infinity')
    exit()

g = defaultdict(int)
num = 1
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if g[i] & g[j]:
            continue
        g[i] |= 1 << num
        g[j] |= 1 << num

        total = 2
        for k in range(n):
            if k in (i, j):
                continue
            x, y = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if is_point_on_line(x, y, x2, y2, x3, y3):
                total += 1
                g[k] |= 1 << num

        ans += (total >= K)
        num += 1
print(ans)
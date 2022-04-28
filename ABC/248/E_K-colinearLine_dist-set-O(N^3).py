from collections import defaultdict

def dist_line_to_point(x1, y1, x2, y2, px, py):
    nmrt = abs((y2 - y1)*px + (x1 - x2)*py + x2*y1 - y2*x1)
    dnmnt = ((y2 - y1)**2 + (x2 - x1)**2) ** 0.5
    return nmrt / dnmnt


n, K = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]

if K == 1:
    print('Infinity')
    exit()

g = defaultdict(lambda : set())
num = 1
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if g[i] & g[j]:
            continue
        g[i].add(num)
        g[j].add(num)

        total = 2
        for k in range(n):
            if k in (i, j):
                continue
            x, y = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if dist_line_to_point(x, y, x2, y2, x3, y3) == 0:
                g[k].add(num)
                total += 1

        num += 1
        ans += (total >= K)
print(ans)
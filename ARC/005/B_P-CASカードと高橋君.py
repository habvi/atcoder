x, y, W = input().split()
x, y = int(x) - 1, int(y) - 1
c = [input() for _ in range(9)]
d = {'R':(0, 1), 'L':(0, -1), 'U':(-1, 0), 'D':(1, 0),
     'RU':(-1, 1), 'RD':(1, 1), 'LU':(-1, -1), 'LD':(1, -1)}
dy, dx = d[W]

ans = ''
for i in range(4):
    ans += c[y][x]
    if (y == 0 and dy < 0) or (y == 8 and dy > 0):
        dy *= -1
    if (x == 0 and dx < 0) or (x == 8 and dx > 0):
        dx *= -1
    y += dy
    x += dx
print(ans)
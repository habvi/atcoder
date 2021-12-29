x, y, W = input().split()
x, y = int(x) - 1, int(y) - 1
c = [input() for _ in range(9)]
dir = ['R', 'L', 'U', 'D', 'RU', 'RD', 'LU', 'LD']
dys = [0, 0, -1, 1, -1, 1, -1, 1]
dxs = [1, -1, 0, 0, 1, 1, -1, -1]
dy = dys[dir.index(W)]
dx = dxs[dir.index(W)]

if W in ('U', 'RU', 'LU') and y == 0 or W in ('D', 'RD', 'LD') and y == 8:
    dy *= -1
if W in ('L', 'LU', 'LD') and x == 0 or W in ('R', 'RU', 'RD') and x == 8:
    dx *= -1

ans = ''
for i in range(4):
    ans += c[y][x]
    y += dy
    x += dx
    if y in (0, 8):
        dy *= -1
    if x in (0, 8):
        dx *= -1
print(ans)
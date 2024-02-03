H, W, N = map(int, input().split())

# up,right,down,left
DXY = [(0, -1), (1, 0), (0, 1), (-1, 0)]

G = [['.'] * W for _ in range(H)]
y, x = 0, 0
dir = 0
for _ in range(N):
    if G[y][x] == '.':
        G[y][x] = '#'
        dir = (dir + 1) % 4
    else:
        G[y][x] = '.'
        dir = (dir - 1) % 4
    y += DXY[dir][1]
    x += DXY[dir][0]
    y %= H
    x %= W

for g in G:
    print(''.join(g))
def draw(start, num, mark):
    for i in range(start, h, 2):
        for j in range(0, w, 2):
            if num <= 0:
                return
            g[i][j] = mark
            num -= 1


A, B = map(int, input().split())

h, w = 100, 100
g = [['.'] * w for _ in range(h)]
for i in range(50, h):
    for j in range(w):
        g[i][j] = '#'

draw(51, A - 1, '.')
draw(0, B - 1, '#')

print(h, w)
for ans in g:
    print(''.join(ans))
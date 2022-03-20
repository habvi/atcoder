n = int(input())
T = input()

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

x, y = 0, 0
now = 1
for t in T:
    if t =='R':
        now += 1
        now %= 4
    else:
        x += d[now][0]
        y += d[now][1]

print(x, y)
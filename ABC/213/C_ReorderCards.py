h, w, n = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

idx = {}
for i, (a, b) in enumerate(ab):
    idx[(a, b)] = i

ans_x = [None] * n
x = [(0, 0), *sorted(ab, key=lambda x: x[1])]
dst = 0
for i in range(n):
    l = x[i][1]
    r = x[i + 1][1]
    dst += max(0, r - l - 1)
    a, b = x[i + 1]
    ans_x[idx[(a, b)]] = r - dst

ans_y = [None] * n
y = [(0, 0), *sorted(ab, key=lambda x: x[0])]
dst = 0
for i in range(n):
    l = y[i][0]
    r = y[i + 1][0]
    dst += max(0, r - l - 1)
    a, b = y[i + 1]
    ans_y[idx[(a, b)]] = r - dst

for y, x in zip(ans_y, ans_x):
    print(y, x)
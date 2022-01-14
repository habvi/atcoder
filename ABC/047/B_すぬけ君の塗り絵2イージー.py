w, h, n = map(int, input().split())
g = [[0] * w for _ in range(h)]
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(h):
            for j in range(x):
                g[i][j] = 1
    elif a == 2:
        for i in range(h):
            for j in range(x, w):
                g[i][j] = 1
    elif a == 3:
        for i in range(y):
            for j in range(w):
                g[i][j] = 1
    else:
        for i in range(y, h):
            for j in range(w):
                g[i][j] = 1

print(sum(gg.count(0) for gg in g))
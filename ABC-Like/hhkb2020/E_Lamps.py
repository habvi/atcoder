h, w = map(int, input().split())
s = [input() for _ in range(h)]
MOD = 10**9 + 7

k = 0
u = [[1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            u[i][j] = 0
            k += 1
            continue
        if i + 1 < h and s[i + 1][j] == '.':
            u[i + 1][j] = u[i][j] + 1

d = [[1] * w for _ in range(h)]
for i in reversed(range(h)):
    for j in range(w):
        if s[i][j] == '#':
            d[i][j] = 0
            continue
        if i - 1 >= 0 and s[i - 1][j] == '.':
            d[i - 1][j] = d[i][j] + 1

l = [[1] * w for _ in range(h)]
for i in reversed(range(h)):
    for j in range(w):
        if s[i][j] == '#':
            l[i][j] = 0
            continue
        if j + 1 < w and s[i][j + 1] == '.':
            l[i][j + 1] = l[i][j] + 1

r = [[1] * w for _ in range(h)]
for i in range(h):
    for j in reversed(range(w)):
        if s[i][j] == '#':
            r[i][j] = 0
            continue
        if j - 1 >= 0 and s[i][j - 1] == '.':
            r[i][j - 1] = r[i][j] + 1

k = h * w - k
tot = pow(2, k, MOD)
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        ar = u[i][j] + d[i][j] + l[i][j] + r[i][j] - 3
        ans += tot - pow(2, k - ar, MOD)
print((ans + MOD) % MOD)
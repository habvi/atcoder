from collections import defaultdict

n = int(input())
D = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n - 1):
        D[i][j + 1] += D[i][j]

for i in range(n - 1):
    for j in range(n):
        D[i + 1][j] += D[i][j]

mx = defaultdict(int)
for ly in range(n):
    for lx in range(n):
        for ry in range(ly, n):
            for rx in range(lx, n):
                total = D[ry][rx]
                if lx - 1 >= 0:
                    total -= D[ry][lx - 1]
                if ly - 1 >= 0:
                    total -= D[ly - 1][rx]
                if ly - 1 >= 0 and lx - 1 >= 0:
                    total += D[ly - 1][lx - 1]

                s = (ry - ly + 1) * (rx - lx + 1)
                mx[s] = max(mx[s], total)

for i in range(1, max(mx) + 1):
    mx[i] = max(mx[i], mx[i - 1])

Q = int(input())
for _ in range(Q):
    p = int(input())
    print(mx[p])
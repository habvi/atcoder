def check(i, j):
    y, x = i, j
    while y >= 0 and x >= 0:
        if G[y][x]:
            return False
        y -= 1
        x -= 1
    y, x = i, j
    while y < N and x < N:
        if G[y][x]:
            return False
        y += 1
        x += 1
    y, x = i, j
    while y >= 0 and x < N:
        if G[y][x]:
            return False
        y -= 1
        x += 1
    y, x = i, j
    while y < N and x >= 0:
        if G[y][x]:
            return False
        y += 1
        x -= 1
    return True


N = int(input())
G = [[0] * N for _ in range(N)]

R = set()
C = set()
for _ in range(N - 1):
    r, c = map(lambda x: int(x) - 1, input().split())
    R.add(r)
    C.add(c)
    G[r][c] = 1

for i in range(N):
    if i not in R:
        break
for j in range(N):
    if j not in C:
        break

if check(i, j):
    print(i + 1, j + 1)
else:
    print(-1)
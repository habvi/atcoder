n = int(input())
dst = [list(map(int, input().split())) for _ in range(n)]

edges = []
for i in range(n):
    for j in range(i + 1, n):
        if i == j:
            continue
        edges.append((dst[i][j], i, j))

erase = set()
for d, i, j in edges:
    for k in range(n):
        if i == k or k == j:
            continue

        if d > dst[i][k] + dst[k][j]:
            print(-1)
            exit()

        if d == dst[i][k] + dst[k][j]:
            erase.add((i, j))

ans = 0
for d, i, j, in edges:
    if (i, j) not in erase:
        ans += d
print(ans)
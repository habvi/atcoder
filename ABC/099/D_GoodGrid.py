from collections import defaultdict

n, C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(C)]
g = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

cost = [defaultdict(int) for _ in range(3)]
for i in range(n):
    for j in range(n):
        k = (i + j) % 3
        X = g[i][j]
        for Y in range(C):
            cost[k][Y] += D[X][Y]

ans = float('inf')
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or j == k or k == i:
                continue

            total = cost[0][i] + cost[1][j] + cost[2][k]
            ans = min(ans, total)
print(ans)
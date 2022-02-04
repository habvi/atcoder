from itertools import permutations

n, m, r = map(int, input().split())
R = list(map(lambda x: int(x) - 1, input().split()))

INF = float('inf')
dst = [[INF] * n for _ in range(n)]

for i in range(n):
    dst[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    dst[a][b] = min(dst[a][b], c)
    dst[b][a] = min(dst[b][a], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j])


def get_dist(R):
    total = 0
    for i in range(1, r):
        total += dst[R[i - 1]][R[i]]
    return total


ans = float('inf')
for per in permutations(R):
    ans = min(ans, get_dist(per))
print(ans)
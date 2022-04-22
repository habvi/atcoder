from itertools import permutations

n, m, r = map(int, input().split())
R = list(map(lambda x: int(x) - 1, input().split()))

INF = float('inf')
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    dist[a][b] = c
    dist[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def get_dist(R):
    total = 0
    for i in range(1, r):
        total += dist[R[i - 1]][R[i]]
    return total


ans = float('inf')
for per in permutations(R):
    ans = min(ans, get_dist(per))
print(ans)
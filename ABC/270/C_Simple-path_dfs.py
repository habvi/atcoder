import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, route):
    if v == Y:
        print(*route)
        exit()
    for nv in g[v]:
        if seen[nv]:
            continue
        seen[nv] = 1
        route.append(nv + 1)
        dfs(nv, route)
        route.pop()


N, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1
g = defaultdict(list)
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

seen = [0] * N
seen[X] = 1
dfs(X, [X + 1])


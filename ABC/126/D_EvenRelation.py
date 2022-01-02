from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p):
    for nv, nw in g[v]:
        if nv == p:
            continue
        if nw % 2 == 0:
            c[nv] = c[v]
        else:
            c[nv] = 1 - c[v]
        dfs(nv, v)

n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    g[u].append((v, w))
    g[v].append((u, w))

c = [-1] * n
c[0] = 0
dfs(0, -1)
print(*c)
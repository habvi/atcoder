import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v):
    seen[v] = 1
    for nv in g[v]:
        if seen[nv]:
            continue
        dfs(nv)
    toposo.append(v)


n, m = map(int, input().split())
g = defaultdict(list)
edge = []
for _ in range(n + m - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    edge.append((a, b))

toposo = []
seen = [0] * n
for i in range(n):
    if seen[i]:
        continue
    dfs(i)

toposo = toposo[::-1]
v_nv = dict(zip(toposo, range(n)))

parent = [-1] * n
for a, b in edge:
    na, nb = v_nv[a], v_nv[b]
    parent[nb] = max(parent[nb], na)

for i in range(n):
    p = parent[v_nv[i]]
    if p == -1:
        print(0)
    else:
        print(toposo[p] + 1)
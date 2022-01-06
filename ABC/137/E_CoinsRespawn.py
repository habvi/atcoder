import sys
sys.setrecursionlimit(10**7)
def dfs(v):
    if from1[v]:
        return
    from1[v] = 1
    for nv in g[v]:
        dfs(nv)

def rdfs(v):
    if toN[v]:
        return
    toN[v] = 1
    for nv in rg[v]:
        rdfs(nv)

from collections import defaultdict
n, m, p = map(int, input().split())
edges = []
g = defaultdict(list)
rg = defaultdict(list)
from1 = [0] * n
toN = [0] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges.append((a, b, -(c - p)))
    g[a].append(b)
    rg[b].append(a)

dfs(0)
rdfs(n - 1)

ok = [0] * n
for i in range(n):
    ok[i] = from1[i] & toN[i]

dst = [float('inf')] * n
dst[0] = 0
cnt = 0
upd = 1
while upd:
    upd = 0
    for i in range(m):
        a, b, c = edges[i]
        if not ok[a] or not ok[b]:
            continue
        ndst = dst[a] + c
        if ndst < dst[b]:
            upd = 1
            dst[b] = ndst
    cnt += 1
    if cnt > n:
        print(-1)
        exit()

ans = -dst[n - 1]
print(max(0, ans))
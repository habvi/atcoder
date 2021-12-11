import sys
sys.setrecursionlimit(10 ** 7)
def dfs1(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        dfs1(nv, v)
        if h[nv]:
            dm[nv] = 1
        dm[v] |= dm[nv]

def dfs2(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        if not dm[nv]:
            continue
        ans[0] += 1
        dfs2(nv, v)
        ans[0] += 1

from collections import defaultdict
n, x = map(int, input().split())
h = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x : int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dm = [0] * n
h[x - 1] = 1
dfs1(x - 1, -1)

ans = [0]
dfs2(x - 1, -1)
print(ans[0])
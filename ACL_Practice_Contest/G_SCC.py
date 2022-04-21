from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

def make_scc(g, rg):
    def dfs1(v):
        seen1[v] = 1
        for nv in g[v]:
            if seen1[nv]:
                continue
            dfs1(nv)
        route.append(v)

    def dfs2(v):
        seen2[v] = 1
        scc_each.append(v)
        for nv in rg[v]:
            if seen2[nv]:
                continue
            dfs2(nv)

    route = []
    seen1 = [0] * n
    for v in range(n):
        if seen1[v]:
            continue
        dfs1(v)

    seen2 = [0] * n
    scc = []
    for v in route[::-1]:
        if seen2[v]:
            continue
        scc_each = []
        dfs2(v)
        scc.append(scc_each)

    return scc


n, m = map(int, input().split())
g = defaultdict(list)
rg = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    rg[b].append(a)

scc = make_scc(g, rg)

print(len(scc))
for s in scc:
    print(len(s), *s)
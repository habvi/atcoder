import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict, deque

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
    seen1 = [0] * N
    for v in range(N):
        if seen1[v]:
            continue
        dfs1(v)

    seen2 = [0] * N
    scc = []
    for v in route[::-1]:
        if seen2[v]:
            continue
        scc_each = []
        dfs2(v)
        scc.append(scc_each)
    return scc

def bfs(u):
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in rg[v]:
            if seen[nv]:
                continue
            seen[nv] = 1
            que.append(nv)


N, M = map(int, input().split())

g = defaultdict(list)
rg = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    rg[b].append(a)

scc = make_scc(g, rg)

seen = [0] * N
for vs in scc:
    if len(vs) == 1:
        continue
    v = vs[0]
    if seen[v]:
        continue
    seen[v] = 1
    bfs(v)
print(sum(seen))
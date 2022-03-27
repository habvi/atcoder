from collections import deque, defaultdict
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


def bfs(u):
    q = deque([u])
    while q:
        v = q.popleft()
        for nv in rg[v]:
            if seen[nv]:
                continue
            seen[nv] = 1
            q.append(nv)


n, m = map(int, input().split())
g = defaultdict(list)
rg = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    rg[b].append(a)

cycle = []
scc = make_scc(g, rg)
for v in scc:
    if len(v) == 1:
        continue
    cycle.extend(v)

seen = [0] * n
for v in cycle:
    if seen[v]:
        continue
    seen[v] = 1
    bfs(v)

print(sum(seen))
from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

def dfs1(v):
    seen1[v] = 1
    for nv in g[v]:
        if seen1[nv]:
            continue
        dfs1(nv)
    route.append(v)

def dfs2(v):
    seen2[v] = 1
    scc.append(v)
    for nv in rg[v]:
        if seen2[nv]:
            continue
        dfs2(nv)

def bfs(u):
    q = deque([u])
    while q:
        v = q.popleft()
        for nv in rg[v]:
            if seen3[nv]:
                continue
            seen3[nv] = 1
            q.append(nv)


n, m = map(int, input().split())
g = defaultdict(list)
rg = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    rg[b].append(a)

route = []
seen1 = [0] * n
for v in range(n):
    if seen1[v]:
        continue
    dfs1(v)

seen2 = [0] * n
cycle = set()
for v in route[::-1]:
    if seen2[v]:
        continue

    scc = []
    dfs2(v)
    if len(scc) >= 2:
        for v in scc:
            cycle.add(v)

seen3 = [0] * n
for v in cycle:
    if seen3[v]:
        continue
    seen3[v] = 1
    bfs(v)

print(sum(seen3))
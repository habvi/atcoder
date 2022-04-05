import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v):
    if front[v]:
        return
    front[v] = 1
    for nv in g[v]:
        dfs(nv)

def rdfs(v):
    if tail[v]:
        return
    tail[v] = 1
    for nv in rg[v]:
        rdfs(nv)

def BellmanFord(st):
    INF = float('inf')
    dist = [INF] * n
    dist[st] = 0
    count_ = 0
    upd = 1
    while upd:
        upd = 0
        for a, b, c in edges:
            if not ok[a] or not ok[b]:
                continue
            ndst = dist[a] + c
            if ndst < dist[b]:
                upd = 1
                dist[b] = ndst
        count_ += 1
        if count_ > n:
            print(-1)
            exit()
    return dist


n, m, P = map(int, input().split())

edges = []
g = defaultdict(list)
rg = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges.append((a, b, -(c - P)))
    g[a].append(b)
    rg[b].append(a)

front = [0] * n
dfs(0)

tail = [0] * n
rdfs(n - 1)

ok = [0] * n
for i in range(n):
    ok[i] = front[i] & tail[i]

dist = BellmanFord(0)

ans = max(0, -dist[n - 1])
print(ans)
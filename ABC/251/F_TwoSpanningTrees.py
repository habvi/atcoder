import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict, deque

def dfs(v):
    for nv in g[v]:
        if seen[nv]:
            continue
        T1.append((v + 1, nv + 1))
        seen[nv] = 1
        dfs(nv)

def bfs(u):
    seen = [0] * n
    seen[u] = 1
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in g[v]:
            if seen[nv]:
                continue
            T2.append((v + 1, nv + 1))
            seen[nv] = 1
            que.append(nv)


n, m = map(int, input().split())
g = defaultdict(list)
for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

T1 = []
seen = [0] * n
seen[0] = 1
dfs(0)
for u, v in T1:
    print(u, v)

T2 = []
bfs(0)
for u, v in T2:
    print(u, v)
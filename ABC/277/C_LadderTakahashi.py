import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v):
    for nv in g[v]:
        if nv in seen:
            continue
        seen.add(nv)
        dfs(nv)


N = int(input())
g = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

seen = set([1])
dfs(1)
print(max(seen))
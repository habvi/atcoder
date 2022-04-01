import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p):
    ans.append(v + 1)
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
        ans.append(v + 1)


n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

for v in range(n):
    g[v].sort()

ans = []
dfs(0, -1)

print(*ans)
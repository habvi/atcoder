import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v):
    global ans
    seen[v] = 1
    if sum(seen) == n:
        ans += 1
        return

    for nv in g[v]:
        if seen[nv]:
            continue
        dfs(nv)
        seen[nv] = 0


n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

seen = [0] * n
ans = 0
dfs(0)

print(ans)
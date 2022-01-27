from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((b, c))
    g[b].append((a, c))

def dfs(v, p):
    seen[v] = 1
    for nv, nc in g[v]:
        if nv == p or seen[nv]:
            continue
        if ans[v] == nc:
            if nc + 1 <= n:
                nc += 1
            else:
                nc = 1
        ans[nv] = nc
        dfs(nv, v)

seen = [0] * n
seen[0] = 1
ans = [0] * n
ans[0] = 1
dfs(0, -1)
print(*ans)
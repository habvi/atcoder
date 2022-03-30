from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p):
    for nv, nw in g[v]:
        if nv == p:
            continue
        if nw % 2 == 0:
            ans[nv] = ans[v]
        else:
            ans[nv] = 1 - ans[v]
        dfs(nv, v)


n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    g[u].append((v, w))
    g[v].append((u, w))

ans = [-1] * n
ans[0] = 0
dfs(0, -1)

print(*ans)
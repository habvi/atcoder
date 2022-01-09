import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p):
    x = k - 1 if p < 0 else k - 2
    for nv in g[v]:
        if nv == p:
            continue
        ans[0] *= x
        ans[0] %= MOD
        x -= 1
        dfs(nv, v)

from collections import defaultdict
n, k = map(int, input().split())
MOD = 10**9 + 7
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

ans = [k]
dfs(0, -1)
print(ans[0])
import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p):
    global ans
    color = (K - 1 if p == -1 else K - 2)
    for nv in g[v]:
        if nv == p:
            continue
        ans *= color
        ans %= MOD
        color -= 1
        dfs(nv, v)


n, K = map(int, input().split())
MOD = 10**9 + 7

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

ans = K
dfs(0, -1)

print(ans)
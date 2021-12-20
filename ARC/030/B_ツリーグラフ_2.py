from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
        if h[nv] or cnt[nv] > 0:
            cnt[v] += cnt[nv] + 2

n, x = map(int, input().split())
x -= 1
h = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

cnt = [0] * n
dfs(x, -1)
print(cnt[x])
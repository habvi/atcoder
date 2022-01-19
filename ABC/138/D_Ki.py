import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        cnt[nv] += cnt[v]
        dfs(nv, v)

from collections import defaultdict
n, q = map(int, input().split())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

cnt = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x

dfs(0, -1)
print(*cnt)
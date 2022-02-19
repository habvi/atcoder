from collections import defaultdict
from bisect import insort
import sys
sys.setrecursionlimit(10 ** 8)

def dfs(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
        for m in num[nv]:
            insort(num[v], m)
            if len(num[v]) > 20:
                num[v].pop(0)


n, q = map(int, input().split())
X = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

num = [[] for _ in range(n)]
for i, x in enumerate(X):
    num[i].append(x)

dfs(0, -1)

for _ in range(q):
    v, k = map(int, input().split())
    v -= 1
    print(num[v][-k])
import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
        if H[nv] or num[nv]:
            num[v] += num[nv] + 2


n, X = map(int, input().split())
X -= 1
H = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

num = [0] * n
dfs(X, -1)

print(num[X])
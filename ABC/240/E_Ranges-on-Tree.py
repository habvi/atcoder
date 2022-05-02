import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p):
    global num
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)

        if L[nv] == INF:
            L[nv] = num
            R[nv] = num
            num += 1

        L[v] = min(L[v], L[nv])
        R[v] = max(R[v], R[nv])


n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

INF = float('inf')
L = [INF] * n
R = [0] * n

num = 1
dfs(0, -1)

for l, r in zip(L, R):
    print(l, r)
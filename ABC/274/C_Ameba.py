import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p, d):
    ans[v - 1] = d
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v, d + 1)


N = int(input())
A = list(map(int, input().split()))

g = defaultdict(list)
for i, a in enumerate(A, 1):
    g[a].append(2 * i)
    g[a].append(2 * i + 1)

ans = [None] * (2 * N + 1)
dfs(1, -1, 0)
print(*ans)
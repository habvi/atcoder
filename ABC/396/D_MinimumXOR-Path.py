import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, xor):
    global ans
    if v == N - 1:
        ans = min(ans, xor)

    visited[v] = True
    for nv, w in g[v]:
        if visited[nv]:
            continue
        dfs(nv, xor ^ w)
    visited[v] = False


N, M = map(int, input().split())
g = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    g[u].append((v, w))
    g[v].append((u, w))

INF = float('inf')
ans = INF
visited = [False] * N
dfs(0, 0)
print(ans)

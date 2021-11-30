import sys
sys.setrecursionlimit(10**7)
def dfs(v, p, d):
    dist[v] = d
    for nv, nd in G[v]:
        if nv == p: continue
        dfs(nv, v, d + nd)

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((b, c))
    G[b].append((a, c))

Q, K = map(int, input().split())
dist = [-1] * n
dfs(K - 1, -1, 0)
for _ in range(Q):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    print(dist[x] + dist[y])
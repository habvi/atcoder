import sys

sys.setrecursionlimit(10**7)
from collections import defaultdict


def dfs(v, p, d, dist):
    dist[v] = d
    for nv, nd in G[v]:
        if nv == p:
            continue
        dfs(nv, v, d + nd, dist)
    return dist


N = int(input())
total_dist = 0
G = defaultdict(list)
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((b, c))
    G[b].append((a, c))
    total_dist += c

dist1 = [-1] * N
dist1 = dfs(0, -1, 0, dist1)

dist2 = [-1] * N
dist2 = dfs(dist1.index(max(dist1)), -1, 0, dist2)

print(total_dist * 2 - max(dist2))

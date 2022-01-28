import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def is_bipartite(v):
    color = [-1] * n
    return bp_dfs(v, color)

def bp_dfs(v, color, c=0):
    color[v] = c
    for nv in g[v]:
        if color[nv] != -1:
            if color[nv] == color[v]:
                return False
            continue
        if not bp_dfs(nv, color, 1 - c):
            return False
    return True

n = int(input())
S = [list(map(int, list(input()))) for _ in range(n)]
g = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        if S[i][j]:
            g[i].append(j)
            g[j].append(i)

if not is_bipartite(0):
    print(-1)
    exit()

dst = S
for i in range(n):
    for j in range(n):
        if i == j:
            dst[i][j] = 0
            continue
        if not dst[i][j]:
            dst[i][j] = float('inf')

for k in range(n):
    for i in range(n):
        for j in range(n):
            dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j])

ans = 0
for i in range(n):
    ans = max(ans, max(dst[i]))
print(ans + 1)
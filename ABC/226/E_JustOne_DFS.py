import sys
sys.setrecursionlimit(10**7)

def dfs(v):
    seen[v] = 1
    # 頂点数
    x[0] += 1
    # 辺の数*2
    y[0] += len(G[v])
    for nv in G[v]:
        if seen[nv]: continue
        dfs(nv)

n, m = map(int, input().split())
MOD = 998244353
G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

seen = [0 for _ in range(n)]
tot, ok = 0, 0
for i in range(n):
    x, y = [0], [0]
    if seen[i]: continue
    dfs(i)
    tot += 1
    if y[0]/2 == x[0]:
        ok += 1
    
if ok == tot:
    print(pow(2, tot, MOD))
else:
    print(0)
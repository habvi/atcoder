import sys
sys.setrecursionlimit(10**7)

def dfs(v):
    seen[v] = 1
    for nv in G[v]:
        if seen[nv]: continue
        dfs(nv)

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

seen = [0]*n
ans = 0
for i in range(n):
    if seen[i]: continue
    dfs(i)
    ans += 1
print(ans - 1)
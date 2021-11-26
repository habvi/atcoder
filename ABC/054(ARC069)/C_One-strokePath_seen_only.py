import sys
sys.setrecursionlimit(10**7)
def dfs(v, cnt):
    seen[v] = 1
    if cnt == n:
        ans[0] += 1
        return
    for nv in G[v]:
        if seen[nv]: continue
        dfs(nv, cnt + 1)
        seen[nv] = 0
    
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

seen = [0]*n
ans = [0]
dfs(0, 1)
print(ans[0])
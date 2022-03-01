import sys
sys.setrecursionlimit(10**7)
def dfs(v, p):
    seen[v] = 1
    rt.append(v)
    if len(rt) == n:
        ans[0] += 1
        # print(rt)
        return
    for nv in G[v]:
        if nv == p: continue
        if seen[nv]: continue
        dfs(nv, v)
        seen[nv] = 0
        rt.pop()
    
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

seen = [0]*n
rt = []
ans = [0]
dfs(0, -1)
print(ans[0])
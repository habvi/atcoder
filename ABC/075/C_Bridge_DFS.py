import sys
sys.setrecursionlimit(10**7)
def dfs(v):
    seen[v] = 1
    for nv in G[v]:
        if seen[nv]: continue
        dfs(nv)

n, m = map(int, input().split())
eg = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

ans = 0
for ps in range(m):
    G = [[] for _ in range(n)]
    for i in range(m):
        if i == ps: continue
        G[eg[i][0]].append(eg[i][1])
        G[eg[i][1]].append(eg[i][0])

    seen = [0]*n
    for i in range(n):
        if G[i]:
            dfs(i)
            break
    if not all(seen):
        ans += 1
print(ans)
import sys
sys.setrecursionlimit(10**7)

def dfs(v, p, cnt):
    if cnt % 2 == 0:
        cl[v] = 1
    for nv, nw in G[v]:
        if nv == p: continue
        if nw % 2 == 1:
            cnt += 1
        dfs(nv, v, cnt)
        if nw % 2 == 1:
            cnt -= 1

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    G[u].append((v, w))
    G[v].append((u, w))
cl = [0]*n
dfs(0, -1, 0)
print(*cl)
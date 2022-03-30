import sys
sys.setrecursionlimit(10**7)

def dfs(v, p, c):
    ans[v] = c
    for nv, nw in G[v]:
        if nv == p:
            continue
        if nw % 2 == 0:
            dfs(nv, v, c)
        else:
            dfs(nv, v, 1 - c)


n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    G[u].append((v, w))
    G[v].append((u, w))

ans = [0] * n
dfs(0, -1, 0)

print(*ans)
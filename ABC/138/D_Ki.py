import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p):
    if p != -1:
        cnt[v] += cnt[p]
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v)
        
n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

cnt = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x

dfs(0, -1)
print(*cnt)
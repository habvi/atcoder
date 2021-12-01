import sys
sys.setrecursionlimit(10**7)
def dfs(v, p):
    ans[v] = c[i[0]]
    for nv in G[v]:
        if nv == p: continue
        i[0] += 1
        dfs(nv, v)

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

c = list(map(int, input().split()))
c.sort(reverse=True)
print(sum(c) - max(c))
ans = [-1] * n
i = [0]
dfs(0, -1)
print(*ans)
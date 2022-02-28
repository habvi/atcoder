import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p, c):
    num = 1
    for nv, i in G[v]:
        if nv == p:
            continue
        if c == num:
            num += 1
        edge[i] = num
        dfs(nv, v, num)
        num += 1


n = int(input())
G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x : int(x) - 1, input().split())
    G[a].append((b, i))
    G[b].append((a, i))

edge = [0] * (n - 1)
dfs(0, -1, -1)

print(max(edge))
print(*edge)
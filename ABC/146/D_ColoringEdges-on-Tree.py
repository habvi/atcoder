from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p, c):
    yet = deque()
    if p != -1:
        edge[ei[(v, p)]] = c
    for i in range(1, len(G[v]) + 1):
        if i != c:
            yet.append(i)
    for nv in G[v]:
        if nv == p: continue
        nc = yet.popleft()
        dfs(nv, v, nc)

n = int(input())
G = [set() for _ in range(n)]
ei = defaultdict(int)
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].add(b)
    G[b].add(a)
    ei[(a, b)] = i
    ei[(b, a)] = i

edge = [0] * (n - 1)
dfs(0, -1, 0)
print(max(set(edge)))
print(*edge)
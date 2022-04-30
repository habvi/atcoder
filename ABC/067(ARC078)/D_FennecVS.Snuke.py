import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict, deque

def ceil(a, b):
    return (a + b - 1) // b

def dfs(v, p, d):
    global mx
    if v == n - 1:
        mx = d
        color[v] = 1
        return True
    for nv in g[v]:
        if nv == p:
            continue
        if dfs(nv, v, d + 1):
            color[v] = (0 if d <= mx // 2 else 1)
            return True
    return False

def bfs(u):
    que = deque([])
    que.append(u)
    seen[u] = 1
    while que:
        v = que.popleft()
        for nv in g[v]:
            if color[nv] != -1 or seen[nv]:
                continue
            color[nv] = color[v]
            seen[nv] = 1
            que.append(nv)


n = int(input())

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

mx = 0
color = [-1] * n
dfs(0, -1, 0)

seen = [0] * n
for v in range(n):
    if color[v] != -1 and not seen[v]:
        bfs(v)

mid = ceil(n, 2)
print('Fennec' if sum(color) < mid else 'Snuke')
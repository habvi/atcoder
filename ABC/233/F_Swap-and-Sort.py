import sys
sys.setrecursionlimit(10**7)
def root(x):
    if rank[x] < 0: return x
    rank[x] = root(rank[x])
    return rank[x]
def unite(x, y):
    x, y = root(x), root(y)
    if x == y: return False
    if rank[x] > rank[y]: x, y = y, x
    rank[x] += rank[y]
    rank[y] = x
    return True
def is_same(x, y): return root(x) == root(y)
def size(x): return -rank[root(x)]

def dfs2(v, tgt, p):
    if P[v] == tgt:
        return True
    for nv, ni in g[v]:
        if nv == p:
            continue
        if dfs2(nv, tgt, v):
            ans.append(ni)
            P[v], P[nv] = P[nv], P[v]
            return True
    return False

def dfs(v, p):
    for nv, ni in g[v]:
        if nv == p:
            continue
        if not dfs(nv, v):
            return False
    if not dfs2(v, v, -1):
        return False
    return True

from collections import defaultdict
n = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))
m = int(input())
rank = [-1] * n
g = defaultdict(list)
for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    if is_same(a, b):
        continue
    g[a].append((b, i + 1))
    g[b].append((a, i + 1))
    unite(a, b)

ans = []
for i in range(n):
    if root(i) == i:
        if not dfs(i, -1):
            print(-1)
            exit()
print(len(ans))
print(*ans)
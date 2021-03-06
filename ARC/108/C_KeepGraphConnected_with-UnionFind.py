from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

def root(x):
    if rank[x] < 0:
       return x
    rank[x] = root(rank[x])
    return rank[x]
def unite(x, y):
    x, y = root(x), root(y)
    if x == y:
        return False
    if rank[x] > rank[y]:
        x, y = y, x
    rank[x] += rank[y]
    rank[y] = x
    return True
def is_same(x, y):
    return root(x) == root(y)
def size(x):
    return -rank[root(x)]

def dfs(v, p):
    for nv, nc in g[v]:
        if nv == p:
            continue
        if ans[v] == nc:
            ans[nv] = (nc + 1 if nc == 1 else 1)
        else:
            ans[nv] = nc
        dfs(nv, v)


n, m = map(int, input().split())

g = defaultdict(list)
rank = [-1] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    if not is_same(a, b):
        unite(a, b)
        g[a].append((b, c))
        g[b].append((a, c))

ans = [0] * n
ans[0] = 1
dfs(0, -1)

print(*ans)
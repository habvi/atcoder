import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

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


n, m = map(int, input().split())
rank = [-1] * n
g = defaultdict(list)
later = []
for _ in range(m):
    l, r, d = map(int, input().split())
    l, r = l - 1, r - 1
    if not is_same(l, r):
        unite(l, r)
        g[l].append((r, d))
        g[r].append((l, -d))
    else:
        later.append((l, r, d))


def dfs(v, p, d):
    depth[v] = d
    for nv, nd in g[v]:
        if nv == p:
            continue
        dfs(nv, v, depth[v] + nd)


depth = [None] * n
for i in range(n):
    if depth[i] is None:
        dfs(i, -1, 0)

for l, r, d in later:
    if depth[r] - depth[l] != d:
        print('No')
        exit()
print('Yes')
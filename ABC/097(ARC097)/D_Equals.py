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

n, m = map(int, input().split())
P = list(map(int, input().split()))
rank = [-1] * n
for i in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    unite(x, y)

from collections import defaultdict
idx = defaultdict(int)
for i, p in enumerate(P):
    idx[p - 1] = i

vs = defaultdict(list)
idxs = defaultdict(list)
for i in range(n):
    rt = root(i)
    vs[rt].append(i)
    idxs[rt].append(idx[i])

ans = 0
for i in range(n):
    if i in vs:
        ans += len(set(vs[i]) & set(idxs[i]))
print(ans)
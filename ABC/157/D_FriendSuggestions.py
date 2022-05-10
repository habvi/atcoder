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


n, m, K = map(int, input().split())

g = defaultdict(list)
rank = [-1] * n
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
    unite(a, b)

for _ in range(K):
    a, b = map(lambda x: int(x) - 1, input().split())
    if is_same(a, b):
        g[a].append(b)
        g[b].append(a)

for i in range(n):
    print(size(i) - len(g[i]) - 1)
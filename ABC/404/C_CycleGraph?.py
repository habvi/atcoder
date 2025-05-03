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


N, M = map(int, input().split())
g = defaultdict(set)
rank = [-1] * N
for _ in range(M):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
    unite(a - 1, b - 1)

if size(0) == N and all(len(v) == 2 for v in g.values()):
    print("Yes")
else:
    print("No")

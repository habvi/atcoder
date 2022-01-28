import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def root(x):
    if rank[x] < 0: return x
    rank[x] = root(rank[x])
    return rank[x]
def unite(x, y):
    x, y = root(x), root(y)
    if x == y:
        edge[x] += 1
        return False
    if rank[x] > rank[y]: x, y = y, x
    rank[x] += rank[y]
    rank[y] = x
    edge[x] += edge[y] + 1
    return True
def is_same(x, y): return root(x) == root(y)
def size(x): return -rank[root(x)]


n, m = map(int, input().split())
rank = [-1] * n
edge = [0] * n
g = defaultdict()
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    unite(a, b)

ans = 0
for i in range(n):
    if i == root(i):
        if edge[root(i)] + 1 == -rank[root(i)]:
            ans += 1
print(ans)
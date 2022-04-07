import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

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


n, m = map(int, input().split())

rank = [-1] * n
p = defaultdict(lambda : -1)
for i in range(n):
    K, *L, = map(lambda x: int(x) - 1, input().split())
    for l in L:
        if p[l] != -1:
            unite(p[l], i)
        p[l] = i

root = sum(1 for r in rank if r < 0)
print('YES' if root == 1 else 'NO')
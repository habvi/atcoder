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

n, q = map(int, input().split())
rank = [-1] * (2*n)
for _ in range(q):
    w, x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    if w == 1:
        if z % 2 == 0:
            unite(x, y)
            unite(x + n, y + n)
        else:
            unite(x, y + n)
            unite(x + n, y)
    else:
        if is_same(x, y):
            print('YES')
        else:
            print('NO')
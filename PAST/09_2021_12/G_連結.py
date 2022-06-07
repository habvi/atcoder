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


n, Q = map(int, input().split())

rank = [-1] * n
edge = defaultdict(int)
for _ in range(Q):
    q, a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if a > b:
        a, b = b, a

    if q == 1:
        edge[(a, b)] += 1
    else:
        for (u, v), num in edge.items():
            if num % 2:
                unite(u, v)

        print('Yes' if is_same(a, b) else 'No')
        rank = [-1] * n
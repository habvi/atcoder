from collections import Counter
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
    return x
def is_same(x, y):
    return root(x) == root(y)
def size(x):
    return -rank[root(x)]


n, q = map(int, input().split())
cls = list(map(lambda x: int(x) - 1, input().split()))

rank = [-1] * n
ct = [Counter([c]) for c in cls]

for _ in range(q):
    t, a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if t == 1:
        if is_same(a, b):
            continue
        
        ra, rb = root(a), root(b)
        r = unite(a, b)
        if r != rb:
            ra, rb = rb, ra
        for k, v in ct[ra].items():
            ct[rb][k] += v
    else:
        print(ct[root(a)][b])
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
    return True
def is_same(x, y):
    return root(x) == root(y)
def size(x):
    return -rank[root(x)]


n, Q = map(int, input().split())
C = list(map(lambda x: int(x) - 1, input().split()))

rank = [-1] * n
num = [Counter([c]) for c in C]

for _ in range(Q):
    q, a, b = map(lambda x: int(x) - 1, input().split())
    if q == 0:
        if is_same(a, b):
            continue

        ra, rb = root(a), root(b)
        unite(a, b)
        if root(b) != rb:
            ra, rb = rb, ra
        for k, v in num[ra].items():
            num[rb][k] += v
    else:
        print(num[root(a)][b])
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


N, M = map(int, input().split())

if N - 1 != M:
    print("No")
    exit()

g = defaultdict(list)
rank = [-1] * N
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
    unite(a, b)

for v in g.values():
    if len(v) > 2:
        print("No")
        exit()

for i, r in enumerate(rank):
    if r < -1 and size(i) == N:
        print("Yes")
        exit()
print("No")
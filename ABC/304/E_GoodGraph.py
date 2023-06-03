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
rank = [-1] * N
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    unite(a, b)

K = int(input())
xy = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]
group = [root(i) for i in range(N)]

ng_connect = set()
for x, y in xy:
    pair = tuple(sorted([group[x], group[y]]))
    ng_connect.add(pair)

Q = int(input())
for _ in range(Q):
    p, q = map(lambda x: int(x) - 1, input().split())
    pair = tuple(sorted([group[p], group[q]]))
    print("No" if pair in ng_connect else "Yes")


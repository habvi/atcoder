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
        edge[x] += 1
        return False
    if rank[x] > rank[y]:
        x, y = y, x
    rank[x] += rank[y]
    rank[y] = x
    edge[x] += edge[y] + 1
    return True
def is_same(x, y):
    return root(x) == root(y)
def uf_size(x):
    return -rank[root(x)]


N, M = map(int, input().split())

rank = [-1] * N
edge = [0] * N
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    unite(a, b)

for v in range(N):
    r = root(v)
    if v == r:
        if uf_size(r) != edge[r]:
            print("No")
            exit()
print("Yes")
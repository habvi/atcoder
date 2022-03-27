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


n, m = map(int, input().split())

rank = [-1] * n
for _ in range(m):
    x, y, z = map(lambda x: int(x) - 1, input().split())
    unite(x, y)

ans = 0
for i in range(n):
    ans += (root(i) == i)

print(ans)
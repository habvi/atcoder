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


n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

edges.sort(key=lambda x: x[2])
rank = [-1] * n
ans = 0
for a, b, w in edges:
    a, b = a - 1, b - 1
    ans += (size(a) * size(b) * w)
    unite(a, b)
print(ans)
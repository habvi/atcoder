import sys
sys.setrecursionlimit(10 ** 7)
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

n, m = map(int, input().split())
rank = [-1] * n
g = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g.append((a, b, c))
g.sort(key=lambda x: x[2])

ans = 0
for a, b, c in g:
    if not is_same(a, b):
        unite(a, b)
    else:
        if c > 0:
            ans += c
print(ans)
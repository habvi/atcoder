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

n, m, k = map(int, input().split())
G = [set() for _ in range(n)]
rank = [-1] * n
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].add(b)
    G[b].add(a)
    unite(a, b)

for _ in range(k):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if is_same(c, d):
        G[c].add(d)
        G[d].add(c)
        unite(c, d)

ans = []
for i in range(n):
    ans.append(size(i) - len(G[i]) - 1)
print(*ans)
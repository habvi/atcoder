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


n, m = map(int, input().split())
eg = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

ans = 0
for ps in range(m):
    rank = [-1 for _ in range(n)]
    for i in range(m):
        if i == ps: continue
        unite(eg[i][0], eg[i][1])

    roots = set()
    for i in range(n):
        roots.add(root(i))

    if len(roots) > 1:
        ans += 1
print(ans)
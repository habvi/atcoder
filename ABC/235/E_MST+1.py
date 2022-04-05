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


n, m, Q = map(int, input().split())

edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edge.append((c, a, b, -1))

for i in range(Q):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edge.append((c, a, b, i))


rank = [-1] * n
edge.sort()
ans = ['No'] * Q
for c, a, b, i in edge:
    if is_same(a, b):
        continue
    if i == -1:
        unite(a, b)
    else:
        ans[i] = 'Yes'

print(*ans)
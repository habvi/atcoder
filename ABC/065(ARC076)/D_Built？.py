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
X, Y = [], []
for i in range(n):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))

X.sort()
Y.sort()

edges = []
for i in range(n - 1):
    (l, li), (r, ri) = X[i], X[i + 1]
    edges.append((abs(l - r), li, ri))

    (l, li), (r, ri) = Y[i], Y[i + 1]
    edges.append((abs(l - r), li, ri))

edges.sort()

rank = [-1] * n
num = n - 1
ans = 0
for cost, u, v in edges:
    if not is_same(u, v):
        unite(u, v)
        ans += cost
        num -= 1

    if not num:
        break
print(ans)
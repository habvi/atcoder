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
q = [tuple(map(int, input().split())) for _ in range(m)]
rank = [-1] * n
ans = n * (n - 1) // 2
lis = [ans]
for a, b in reversed(q[1:]):
    a -= 1; b -= 1
    if not is_same(a, b):
        ans -= size(a) * size(b)
        unite(a, b)
    lis.append(ans)

for a in lis[::-1]:
    print(a)
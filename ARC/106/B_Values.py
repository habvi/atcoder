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
a = list(map(int, input().split()))
b = list(map(int, input().split()))
rank = [-1] * n
for _ in range(m):
    c, d = map(int, input().split())
    c -= 1; d -= 1
    unite(c, d)

sum_a = [0] * n
sum_b = [0] * n
for i in range(n):
    sum_a[root(i)] += a[i]
    sum_b[root(i)] += b[i]
print('Yes' if sum_a == sum_b else 'No')

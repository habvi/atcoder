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
q = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
rank = [-1] * n
tot = (n - 1) * n // 2
ans = [tot]
for a, b in reversed(q[1:]):
    if not is_same(a, b):
        tot -= size(a) * size(b)
        unite(a, b)
    ans.append(tot)

for a in ans[::-1]:
    print(a)
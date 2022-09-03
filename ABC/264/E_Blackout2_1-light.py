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


N, M, E = map(int, input().split())
ab = []
for _ in range(E):
    a, b = map(lambda x: int(x) - 1, input().split())
    ab.append((min(a, N), min(b, N)))

Q = int(input())
X = [int(input()) - 1 for _ in range(Q)]
ng = set(X)

rank = [-1] * (N + 1)
for i, (a, b) in enumerate(ab):
    if i not in ng:
        unite(a, b)

ans = [0] * Q
for i, x in zip(range(Q)[::-1], X[::-1]):
    ans[i] = size(N) - 1
    a, b = ab[x]
    unite(a, b)
print(*ans)

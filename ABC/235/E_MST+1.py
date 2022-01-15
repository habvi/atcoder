from heapq import heapify, heappop, heappush
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

n, m, q = map(int, input().split())
rank = [-1] * n
hq = []
heapify(hq)
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    heappush(hq, (c, a, b, -1))
for i in range(q):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    heappush(hq, (c, a, b, i))

ans = [0] * q
while hq:
    c, a, b, i = heappop(hq)
    if not is_same(a, b):
        if i == -1:
            unite(a, b)
        else:
            ans[i] = 1

for a in ans:
    print('Yes' if a else 'No')
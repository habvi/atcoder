from heapq import heapify, heappop, heappush
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

n = int(input())
X, Y = [], []
for i in range(n):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
X.sort()
Y.sort()

hq = []
heapify(hq)
for i in range(n - 1):
    heappush(hq, (X[i + 1][0] - X[i][0], X[i + 1][1], X[i][1]))
for i in range(n - 1):
    heappush(hq, (Y[i + 1][0] - Y[i][0], Y[i + 1][1], Y[i][1]))

rank = [-1] * n
cnt = 0
cost = 0
while hq and cnt < n - 1:
    d, u, v = heappop(hq)
    if not is_same(u, v):
        unite(u, v)
        cnt += 1
        cost += d
print(cost)
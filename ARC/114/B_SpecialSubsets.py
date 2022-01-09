# 解説後
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
f = list(map(lambda x: int(x) - 1, input().split()))
MOD = 998244353
rank = [-1] * n
for i in range(n):
    unite(i, f[i])

ans = 1
for i in range(n):
    if root(i) == i:
        ans *= 2
        ans %= MOD
print(ans - 1)
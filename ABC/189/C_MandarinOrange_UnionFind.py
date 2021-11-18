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
A = list(map(int,input().split()))
rank = [-1] * n
sa = sorted([[a, i] for i,a in enumerate(A)], reverse=True)

ans = 0
for a, i in sa:
    if i > 0 and A[i-1] >= a:
        unite(i-1, i)
    if i < n-1 and a <= A[i+1]:
        unite(i, i+1)
    ans = max(ans, size(i)*a)
print(ans)
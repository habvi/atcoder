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
    if y in par:
        par.remove(y)
    par.add(x)
    return True
def is_same(x, y): return root(x) == root(y)
def size(x): return -rank[root(x)]

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

rank = [-1] * n
ans = [0]
par = set()
for i in range(n - 1, -1, -1):
    cnt = 0
    for nv in G[i]:
        if nv > i:
            cnt += 1
            unite(nv, i)
    if cnt == 0:
        par.add(i)
    ans.append(len(par))
print(*ans[::-1][1:])
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
    unite_cnt[0] += 1
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
unite_cnt = [0]
for i in range(n - 1):
    ri = n - i - 1
    cnt = 0
    for nv in G[ri]:
        if nv > ri:
            cnt += 1
            unite(nv, ri)
    ans.append(i + 1 - unite_cnt[0])
print(*ans[::-1])
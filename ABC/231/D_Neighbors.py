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

from collections import defaultdict
n, m = map(int, input().split())
g = defaultdict(list)
rank = [-1] * n
for _ in range(m):
    a, b = map(lambda x : int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
    unite(a, b)

par = defaultdict(list)
for i, r in enumerate(rank):
    par[root(i)].append(i)

for k, vs in par.items():
    cnt = defaultdict(int)
    if len(vs) == 1:
        continue
    for v in vs:
        if v in g:
            cnt[len(g[v])] += 1

    lc = len(cnt)
    ks = sorted(cnt.keys())
    if ks == [1, 2] and cnt[1] == 2:
        continue
    elif ks == [1]:
        continue
    else:
        print('No')
        exit()
print('Yes')
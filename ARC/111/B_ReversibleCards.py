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
c = 400001
rank = [-1] * c
seen = set()
cnt = [0] * c
for _ in range(n):
    a, b = map(lambda x: int(x) - 1, input().split())
    seen.add(a)
    seen.add(b)
    cnt[a] += 1
    cnt[b] += 1
    if not is_same(a, b):
        unite(a, b)

from collections import defaultdict
par = defaultdict(list)
for i, r in enumerate(rank):
    if i in seen:
        par[root(i)].append(i)

ans = 0
for p, chs in par.items():
    sm = 0
    for ch in chs:
        sm += cnt[ch]
    ans += min(sm // 2, size(p))
print(ans)
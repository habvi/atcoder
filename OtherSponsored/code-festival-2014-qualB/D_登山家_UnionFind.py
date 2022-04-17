from collections import defaultdict
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


n = int(input())
H = []
hi = defaultdict(list)
for i in range(n):
    h = int(input())
    H.append(h)
    hi[h].append(i)

rank = [-1] * n
ans = [None] * n
for h in sorted(hi.keys()):
    for i in hi[h]:
        if i > 0 and H[i - 1] <= H[i]:
            unite(i, i - 1)
        if i < n - 1 and H[i] >= H[i + 1]:
            unite(i, i + 1)

    for i in hi[h]:
        ans[i] = size(i) - 1

print('\n'.join(map(str, ans)))
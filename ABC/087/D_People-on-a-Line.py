import sys
sys.setrecursionlimit(10 ** 7)

def root(x):
    if par[x] == x:
        return x
    r = root(par[x])
    diff_w[x] += diff_w[par[x]]
    par[x] = r
    return par[x]
def unite(x, y, w):
    w += weight(x) - weight(y)
    x, y = root(x), root(y)
    if x == y: 
        return False
    if rank[x] < rank[y]:
        x, y = y, x
        w *= -1
    if rank[x] == rank[y]:
        rank[x] += 1
    par[y] = x
    diff_w[y] = w
    return True
def is_same(x, y):
    return root(x) == root(y)
def size(x):
    return rank[root(x)]
def weight(x):
    root(x)
    return diff_w[x]
def diff(x, y):
    return weight(y) - weight(x)


n, m = map(int, input().split())

par = list(range(n))
rank = [0] * n
diff_w = [0] * n
for _ in range(m):
    l, r, d = map(int, input().split())
    l, r = l - 1, r - 1
    if is_same(l, r):
        if diff(l, r) != d:
            print('No')
            exit()
    else:
        unite(l, r, d)
print('Yes')
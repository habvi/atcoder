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

def dist_two_points(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def range_check(r1, r2, d):
    return ((r1 - r2) ** 2 <= d <= (r1 + r2) ** 2)

def is_on_circle(x, y, r, x2, y2):
    return (x2 - x) ** 2 + (y2 - y) ** 2 == r ** 2


n = int(input())
sx, sy, tx, ty = map(int, input().split())
circle = [tuple(map(int, input().split())) for _ in range(n)]

rank = [-1] * n
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, r1 = circle[i]
        x2, y2, r2 = circle[j]
        if range_check(r1, r2, dist_two_points(x1, y1, x2, y2)):
            unite(i, j)

cand_s = []
cand_t = []
for i, (x, y, r) in enumerate(circle):
    if is_on_circle(x, y, r, sx, sy):
        cand_s.append(i)
    if is_on_circle(x, y, r, tx, ty):
        cand_t.append(i)

for s in cand_s:
    for t in cand_t:
        if is_same(s, t):
            print('Yes')
            exit()
print('No')
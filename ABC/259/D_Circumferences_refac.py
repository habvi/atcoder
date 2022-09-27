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
    return (x2 - x1)**2 + (y2 - y1)**2

def has_intersection(r1, r2, d):
    return abs(r1 - r2) <= d <= (r1 + r2)


N = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = [tuple(map(int, input().split())) for _ in range(N)]

xyr.append((sx, sy, 0))
xyr.append((tx, ty, 0))

rank = [-1] * (N + 2)
for i in range(N + 2):
    for j in range(i + 1, N + 2):
        x1, y1, r1 = xyr[i]
        x2, y2, r2 = xyr[j]
        dist = dist_two_points(x1, y1, x2, y2)
        if has_intersection(r1, r2, dist):
            unite(i, j)
print("Yes" if is_same(N, N + 1) else "No")

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


def dist_two_points(x1, y1, x2, y2) -> float:
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


N, D = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(N)]

rank = [-1] * N
for i, (x1, y1) in enumerate(xy):
    for j in range(i + 1, N):
        x2, y2 = xy[j]
        if dist_two_points(x1, y1, x2, y2) <= D:
            unite(i, j)

for i in range(N):
    print("Yes" if is_same(0, i) else "No")
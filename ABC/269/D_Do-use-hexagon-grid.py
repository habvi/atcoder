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


N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

DXY = [(-1, -1), (1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)]
rank = [-1] * N
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        for di, dj in DXY:
            ni, nj = x1 + di, y1 + dj
            if (ni, nj) == (x2, y2):
                unite(i, j)
ans = 0
for r in rank:
    ans += (r < 0)
print(ans)

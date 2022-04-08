import sys
sys.setrecursionlimit(10 ** 7)

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

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
    black[x] += black[y]
    white[x] += white[y]
    rank[y] = x
    return True
def is_same(x, y):
    return root(x) == root(y)
def size(x):
    return -rank[root(x)]

def new(y, x):
    return y * w + x


h, w = map(int, input().split())
S = [input() for _ in range(h)]

hw = h * w
seen = [[0] * w for _ in range(h)]
rank = [-1] * hw
black = [0] * hw
white = [0] * hw

for y in range(h):
    for x in range(w):
        if not seen[y][x]:
            black[new(y, x)] += (S[y][x] == '#')
            white[new(y, x)] += (S[y][x] == '.')
            seen[y][x] = 1

        for dy, dx in DXY:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if not seen[ny][nx]:
                black[new(ny, nx)] += (S[ny][nx] == '#')
                white[new(ny, nx)] += (S[ny][nx] == '.')
                seen[ny][nx] = 1
            if S[y][x] == S[ny][nx]:
                continue

            unite(new(y, x), new(ny, nx))

ans = 0
for i in range(hw):
    if root(i) == i:
        ans += black[i] * white[i]
print(ans)
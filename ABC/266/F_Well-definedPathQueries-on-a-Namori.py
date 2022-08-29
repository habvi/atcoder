import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p):
    global start
    seen[v] = 1
    route.append(v)
    for nv in g[v]:
        if finished[nv]:
            continue
        if nv == p:
            continue
        if seen[nv] and not finished[nv]:
            start = nv
            return
        dfs(nv, v)
        if start is not None:
            return
    route.pop()
    finished[v] = 1

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

def dfs2(v, p):
    for nv in g[v]:
        if nv == p or nv in cycle:
            continue
        unite(nv, v)
        dfs2(nv, v)


N = int(input())
g = defaultdict(list)
for _ in range(N):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

seen = [0] * N
finished = [0] * N
route = []
start = None
dfs(0, -1)

cycle = set()
while route:
    v = route.pop()
    cycle.add(v)
    if v == start:
        break

rank = [-1] * N
for v in cycle:
    dfs2(v, -1)

Q = int(input())
for _ in range(Q):
    x, y = map(lambda x: int(x) - 1, input().split())
    print("Yes" if is_same(x, y) else "No")

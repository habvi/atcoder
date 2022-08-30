from collections import defaultdict, deque
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
g = defaultdict(list)
in_deg = [0] * N
for _ in range(N):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
    in_deg[a] += 1
    in_deg[b] += 1

seen = [0] * N
que = deque([])
for v, num in enumerate(in_deg):
    if num == 1:
        que.append(v)
        seen[v] = 1

rank = [-1] * N
while que:
    v = que.popleft()
    for nv in g[v]:
        if seen[nv]:
            continue
        in_deg[nv] -= 1
        unite(nv, v)
        if in_deg[nv] <= 1:
            que.append(nv)
            seen[nv] = 1

Q = int(input())
for _ in range(Q):
    x, y = map(lambda x: int(x) - 1, input().split())
    print("Yes" if is_same(x, y) else "No")
from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10 ** 7)

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

def bfs(u):
    depth[u] = 0
    q = deque([u])
    while q:
        v = q.popleft()
        for nv, nc in g[v]:
            if depth[nv] != -1:
                continue
            depth[nv] = depth[v] + 1
            par[nv] = v
            costs[nv] = nc
            q.append(nv)

n, m, q = map(int, input().split())
cab = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    cab.append((c, a, b))
cab.sort()
 
rank = [-1] * n
g = defaultdict(list)
for c, a, b in cab:
    if not is_same(a, b):
        unite(a, b)
        g[a].append((b, c))
        g[b].append((a, c))
 
par = [-1] * n
costs = [-1] * n
depth = [-1] * n
bfs(0)

def build(par, cost):
    kpar = [par]
    kcost = [cost]
    S = par
    S2 = cost
    for j in range(lenb):
        T = [0] * n
        T2 = [0] * n
        for i in range(n):
            T[i] = S[S[i]]
            T2[i] = max(S2[i], S2[kpar[j][i]])
        kpar.append(T)
        kcost.append(T2)
        S = T
        S2 = T2
    return kpar, kcost

lenb = (n - 1).bit_length()
kpar, kcost = build(par, costs)

def lca(u, v):
    dst = depth[v] - depth[u]
    if dst < 0:
        u, v = v, u
        dst *= -1
    for k in range(lenb + 1):
        if dst & 1:
            v = kpar[k][v]
        dst >>= 1
    if u == v:
        return u
    for k in range(lenb - 1, -1, -1):
        pu = kpar[k][u]
        pv = kpar[k][v]
        if pu != pv:
            u, v = pu, pv
    return kpar[0][u]

def get_max_uv(u, v):
    anc = lca(u, v)
    dst_u = depth[u] - depth[anc]
    dst_v = depth[v] - depth[anc]
    max_u, max_v = -1, -1
    for i in range(lenb):
        if dst_u >> i & 1:
            max_u = max(max_u, kcost[i][u])
            u = kpar[i][u]
    for i in range(lenb):
        if dst_v >> i & 1:
            max_v = max(max_v, kcost[i][v])
            v = kpar[i][v]
    return max(max_u, max_v)
                
for _ in range(q):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    print('Yes' if get_max_uv(u, v) > w else 'No')
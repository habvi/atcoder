from collections import defaultdict, deque

def bfs1(u):
    dist = [-1] * N
    dist[u] = 0
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv, ni in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            par[nv] = (v, ni)
            que.append(nv)
    return dist

def bfs2(u):
    dist = [-1] * N
    dist[u] = 0
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    return dist


N, M = map(int, input().split())
edge = []
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    edge.append((a, b, i))

g = defaultdict(list)
for a, b, i in edge:
    g[a].append((b, i))
par = {}
dist = bfs1(0)
if dist[-1] == -1:
    for _ in range(M):
        print(-1)
    exit()

p = N - 1
route = set()
while p != 0:
    p, i = par[p]
    route.add(i)

mn = dist[-1]
for ei in range(M):
    if ei not in route:
        print(mn)
        continue
    g = defaultdict(list)
    for a, b, i in edge:
        if ei == i:
            continue
        g[a].append(b)
    dist = bfs2(0)
    print(dist[-1])
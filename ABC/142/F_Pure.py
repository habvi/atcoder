from collections import defaultdict, deque

def restore_path(v, dist):
    route = []
    route.append(v + 1)
    while dist[v]:
        for nv in rg[v]:
            if dist[nv] == dist[v] - 1:
                route.append(nv + 1)
                v = nv
                break
    return route

def bfs(u):
    global mn
    dist = [-1] * N
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
            if nv == u and dist[nv] < mn:
                return restore_path(u, dist)
    return []


N, M = map(int, input().split())
g = defaultdict(list)
rg = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    rg[b].append(a)

mn = float('inf')
ans = None
for v in range(N):
    route = bfs(v)
    if route:
        mn = len(route)
        ans = route

if ans is None:
    print(-1)
else:
    print(len(ans))
    for v in ans:
        print(v)
from collections import deque, defaultdict

def bfs(u):
    dist = [-1] * N
    dist[u] = 0
    que = deque([])
    que.append(u)
    pre = [-1] * N
    while que:
        v = que.popleft()
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
            pre[nv] = v
    return pre

def get_route(start, end, parent):
    v = end
    route = [v]
    while True:
        route.append(parent[v])
        if parent[v] == start:
            break
        v = parent[v]
    return route

def bfs2(route):
    dist = [-1] * N
    for v in route:
        dist[v] = 1
    que = deque(route)
    while que:
        v = que.popleft()
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    return dist


N, S, T = map(int, input().split())
g = defaultdict(list)
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

parent = bfs(S - 1)
route = get_route(S - 1, T - 1, parent)
dist = bfs2(route)
print(*dist)
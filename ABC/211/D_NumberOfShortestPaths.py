from collections import deque, defaultdict

def bfs(u):
    dist = [-1] * n
    dist[u] = 0
    q = deque([u])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                route[nv] += route[v]
                q.append(nv)
            else:
                if dist[nv] == dist[v] + 1:
                    route[nv] += route[v]
                    route[nv] %= MOD


n, m = map(int, input().split())
MOD = 10**9 + 7

g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

route = [0] * n
route[0] = 1
bfs(0)

print(route[-1])
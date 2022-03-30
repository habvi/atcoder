from collections import deque, defaultdict

def bfs(u):
    dist = [-1] * n
    dist[u] = 0
    q = deque([u])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    return dist


n, Q = map(int, input().split())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dist = bfs(0)

for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print('Road' if (dist[c] - dist[d]) % 2 else 'Town')
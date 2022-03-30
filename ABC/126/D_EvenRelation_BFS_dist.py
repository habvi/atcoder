from collections import deque, defaultdict

def bfs(u):
    dist = [-1] * n
    dist[u] = 0
    q = deque([u])
    while q:
        v = q.popleft()
        for nv, nc in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + nc
            q.append(nv)
    return dist


n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((b, c))
    g[b].append((a, c))

dist = bfs(0)

for i in range(n):
    print(0 if dist[i] % 2 else 1)
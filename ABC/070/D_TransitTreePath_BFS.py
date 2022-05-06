from collections import defaultdict, deque

def bfs(u):
    dist = [-1] * n
    dist[u] = 0
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv, nc in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + nc
            que.append(nv)
    return dist


n = int(input())
g = defaultdict(list)
for i in range(n - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((b, c))
    g[b].append((a, c))

Q, K = map(int, input().split())
K -= 1

dist = bfs(K)

for _ in range(Q):
    x, y = map(lambda x: int(x) - 1, input().split())
    print(dist[x] + dist[y])
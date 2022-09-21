from collections import defaultdict, deque

def bfs(u):
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
            d[dist[nv]] += 1
            que.append(nv)
    return dist


N, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1
g = defaultdict(list)
for i in range(N - 1):
    g[i].append(i + 1)
    g[i + 1].append(i)
g[X].append(Y)
g[Y].append(X)

d = defaultdict(int)
for v in range(N):
    bfs(v)

for k in range(1, N):
    print(d[k] // 2)
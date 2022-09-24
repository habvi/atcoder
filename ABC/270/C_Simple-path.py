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
            par[nv] = v
            que.append(nv)


N, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1
g = defaultdict(list)
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

par = [-1] * N
bfs(X)

v = Y
ans = [v + 1]
while v != X:
    v = par[v]
    ans.append(v + 1)
print(*ans[::-1])
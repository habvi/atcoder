from collections import deque, defaultdict
def bfs(u):
    dist[u] = 0
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in g[v]:
            if dist[nv] != -1: continue
            dist[nv] = dist[v] + 1
            par[nv] = v
            que.append(nv)
    return dist

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
dist = [-1] * n
par = [-1] * n
bfs(0)

par = par[1:]
if -1 in par:
    print('No')
else:
    print('Yes')
    for ans in par:
        print(ans + 1)
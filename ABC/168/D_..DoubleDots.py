from collections import deque, defaultdict

def bfs(u):
    dist[u] = 0
    q = deque([])
    q.append(u)
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            ans[nv] = v
            q.append(nv)


n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dist = [-1] * n
ans = [-1] * n
bfs(0)

print('Yes')
print(*ans[1:])
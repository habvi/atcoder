from collections import deque, defaultdict

def bfs(u):
    dist[u][0] = 0
    q = deque([])
    q.append((u, 0))
    while q:
        v, rem = q.popleft()
        for nv in g[v]:
            nr = (rem + 1) % 3
            if dist[nv][nr] != -1:
                continue
            dist[nv][nr] = dist[v][rem] + 1
            q.append((nv, nr))


n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)

S, T = map(lambda x: int(x) - 1, input().split())

dist = [[-1] * 3 for _ in range(n)]
bfs(S)

print(dist[T][0] // 3)
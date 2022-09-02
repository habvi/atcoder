from collections import defaultdict, deque

def bfs(u):
    dist = [[-1] * 3 for _ in range(N)]
    dist[u][0] = 0
    que = deque([])
    que.append((u, 0))
    while que:
        v, mod = que.popleft()
        nmod = (mod + 1) % 3
        for nv in g[v]:
            if dist[nv][nmod] != -1:
                continue
            dist[nv][nmod] = dist[v][mod] + 1
            que.append((nv, nmod))
    return dist


N, M = map(int, input().split())
g = defaultdict(list)
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)

S, T = map(lambda x: int(x) - 1, input().split())

dist = bfs(S)
print(dist[T][0] // 3)

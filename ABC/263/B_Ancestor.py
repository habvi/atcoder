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
            que.append(nv)
    return dist


N = int(input())
P = list(map(int, input().split()))

g = defaultdict(list)
for i, p in enumerate(P, 1):
    p -= 1
    g[i].append(p)
    g[p].append(i)

dist = bfs(0)
print(dist[N - 1])
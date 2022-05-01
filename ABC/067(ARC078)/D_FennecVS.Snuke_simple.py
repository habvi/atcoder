from collections import defaultdict, deque

def bfs(u):
    dist = [-1] * n
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


n = int(input())

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

from_1 = bfs(0)
from_n = bfs(n - 1)

fennec, snuke = 0, 0
for v in range(n):
    if from_1[v] <= from_n[v]:
        fennec += 1
    else:
        snuke += 1

print('Fennec' if fennec > snuke else 'Snuke')
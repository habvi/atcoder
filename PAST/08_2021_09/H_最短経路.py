from collections import defaultdict, deque

def bfs(u):
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nc, nv in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + nc
            que.append(nv)


n, X = map(int, input().split())
g = defaultdict(list)
for i in range(n - 1):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((c, b))
    g[b].append((c, a))

for i in range(n):
    dist = [-1] * n
    dist[i] = 0
    bfs(i)

    for j in range(i + 1):
        if dist[j] == X:
            print('Yes')
            exit()
print('No')
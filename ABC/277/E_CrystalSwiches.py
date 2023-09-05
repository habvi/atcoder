from collections import defaultdict, deque

def bfs(st):
    dist = [INF] * N2
    dist[st] = 0
    que = deque([])
    que.append((0, st))
    while que:
        d, v = que.popleft()
        if dist[v] > d:
            continue
        for cost, nv in g[v]:
            nd = d + cost
            if dist[nv] <= nd:
                continue
            dist[nv] = nd
            if cost:
                que.append((nd, nv))
            else:
                que.appendleft((nd, nv))
    return dist


N, M, K = map(int, input().split())
g = defaultdict(list)
N2 = N * 2
for i in range(M):
    x, y, a = map(int, input().split())
    x -= 1
    y -= 1
    if a:
        g[x].append((1, y))
        g[y].append((1, x))
    else:
        g[y + N].append((1, x + N))
        g[x + N].append((1, y + N))
s = list(map(lambda x: int(x) - 1, input().split()))
for v in s:
    g[v].append((0, v + N))
    g[v + N].append((0, v))

INF = float('inf')
dist = bfs(0)
ans = min(dist[N - 1], dist[N2 - 1])
print(ans if ans != INF else -1)
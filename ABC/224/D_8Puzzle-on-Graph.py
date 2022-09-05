from collections import defaultdict, deque

def bfs(u):
    dist[u] = 0
    que = deque([])
    que.append(u)
    while que:
        P = que.popleft()
        v = P.index(9)
        for nv in g[v]:
            p = list(P)
            p[v], p[nv] = p[nv], p[v]
            tp = tuple(p)
            if dist[tp] != -1:
                continue
            dist[tp] = dist[P] + 1
            que.append(tp)


M = int(input())
g = defaultdict(list)
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
P = list(map(int, input().split()))

dist = defaultdict(lambda : -1)
start = [9] * 9
for i, p in enumerate(P):
    start[p - 1] = i + 1
bfs(tuple(start))

target = tuple(range(1, 10))
ans = dist[target]
print(ans)
from collections import deque

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

def bfs2(u):
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in g[v]:
            if dist[v] < dist[nv]:
                num[nv] += num[v]
                que.append(nv)


n = int(input())

g = [[] for _ in range(n)]
edge = []
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
    edge.append((a, b))

dist = bfs(0)

Q = int(input())
num = [0] * n
for _ in range(Q):
    t, e, x = map(int, input().split())
    a, b = edge[e - 1]
    if t == 2:
        a, b = b, a

    if dist[a] < dist[b]:
        num[0] += x
        num[b] -= x
    else:
        num[a] += x

bfs2(0)
print(*num)
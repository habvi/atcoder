from collections import defaultdict, deque

def bfs(u):
    dst = [-1] * n
    dst[u] = 0
    q = deque([u])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dst[nv] != -1:
                continue
            dst[nv] = dst[v] + 1
            q.append(nv)
    return dst

n = int(input())
g = defaultdict(list)
edge = []
for _ in range(n - 1):
    a, b  = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
    edge.append((a, b))

dst = bfs(0)

q = int(input())
cnt = [0] * n
for _ in range(q):
    t, e, x = map(int, input().split())
    e -= 1
    a, b = edge[e]
    if t == 2:
        a, b = b, a
    
    if dst[a] < dst[b]:
        cnt[0] += x
        cnt[b] -= x
    else:
        cnt[a] += x

def bfs2(u):
    q = deque([u])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dst[nv] > dst[v]:
                cnt[nv] += cnt[v]
                q.append(nv)

bfs2(0)
print(*cnt)
from collections import defaultdict, deque

def bfs(u):
    seen = [0] * N
    seen[u] = 1
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in g[v]:
            if seen[nv]:
                continue
            num[nv] += num[v]
            seen[nv] = 1
            que.append(nv)


N, Q = map(int, input().split())

g = defaultdict(list)
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

num = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    num[p] += x

bfs(0)
print(*num)

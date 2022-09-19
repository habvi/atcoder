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
            seen[nv] = 1
            que.append(nv)
    return sum(seen)


N, M = map(int, input().split())
g = defaultdict(list)
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)

ans = 0
for i in range(N):
    ans += bfs(i)
print(ans)

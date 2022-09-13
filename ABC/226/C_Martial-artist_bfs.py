from collections import defaultdict, deque

def bfs(u):
    ans = T[-1]
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
            ans += T[nv]
            que.append(nv)
    return ans


N = int(input())
g = defaultdict()
T = []
for v in range(N):
    t, _, *a = map(int, input().split())
    T.append(t)
    g[v] = tuple(map(lambda x: x - 1, a))
print(bfs(N - 1))
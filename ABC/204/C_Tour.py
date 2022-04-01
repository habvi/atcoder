from collections import deque, defaultdict

def bfs(u):
    seen[u] = 1
    q = deque([u])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if seen[nv]:
                continue
            seen[nv] = 1
            q.append(nv)
    return seen


n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)

ans = 0
for i in range(n):
    seen = [0] * n
    bfs(i)
    ans += sum(seen)

print(ans)
from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)

INF = float('inf')
mn = [INF] * n
ans = -INF
for v in range(n):
    for nv in g[v]:
        mn[nv] = min(mn[nv], mn[v], A[v])
        ans = max(ans, A[nv] - mn[nv])
        mn[nv] = min(mn[nv], A[nv])
print(ans)
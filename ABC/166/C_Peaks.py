from collections import defaultdict

N, M = map(int, input().split())
H = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(H[b])
    g[b].append(H[a])

ans = 0
for v, h in enumerate(H):
    if not g[v] or max(g[v]) < h:
        ans += 1
print(ans)
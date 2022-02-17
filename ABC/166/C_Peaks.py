from collections import defaultdict

n, m = map(int, input().split())
H = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

ans = 0
for v, h in enumerate(H):
    high = True
    for nv in g[v]:
        if h <= H[nv]:
            high = False
            break
    ans += high

print(ans)
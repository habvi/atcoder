from itertools import permutations

n, m = map(int, input().split())
G = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].add(b)
    G[b].add(a)

ans = 0
for per in permutations(range(1, n + 1)):
    v = 0
    for nv in per:
        if nv not in G[v]:
            break
        v = nv
    else:
        ans += 1
print(ans)
from itertools import permutations
n, m = map(int, input().split())
G = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].add(b)
    G[b].add(a)

ans = 0
for per in permutations([i for i in range(1, n)]):
    v = 0
    for nv in per:
        if nv not in G[v]:
            break
        v = nv
    else:
        ans += 1
print(ans)
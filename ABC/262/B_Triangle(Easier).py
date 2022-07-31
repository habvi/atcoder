from collections import defaultdict

N, M = map(int, input().split())

g = defaultdict(set)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].add(b)
    g[b].add(a)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if i in g[j] and j in g[k] and k in g[i]:
                ans += 1
print(ans)
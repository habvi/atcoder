from collections import defaultdict

N, M = map(int, input().split())

g = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b + 1)
    g[b].append(a + 1)

for i in range(N):
    print(len(g[i]), *sorted(g[i]))
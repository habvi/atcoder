from collections import defaultdict, deque

n, m = map(int, input().split())
g = defaultdict(list)
edge = defaultdict(int)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[b].append(a)
    edge[a] += 1

deg = deque()
for i in range(n):
    if not edge[i]:
        deg.append(i)

ans = [1] * n
while deg:
    v = deg.popleft()
    ans[v] = 0
    for nv in g[v]:
        edge[nv] -= 1
        if not edge[nv]:
            deg.append(nv)

print(sum(ans))
from collections import defaultdict, deque

n, m = map(int, input().split())

g = defaultdict(list)
edges = []
indeg = defaultdict(int)
for _ in range(n - 1 + m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
    edges.append((a, b))
    indeg[b] += 1

q = deque([])
for i in range(n):
    if not indeg[i]:
        q.append(i)

topo = []
while q:
    v = q.popleft()
    topo.append(v)
    for nv in g[v]:
        indeg[nv] -= 1
        if not indeg[nv]:
            q.append(nv)

new = dict(zip(topo, range(n)))

parent = [-1] * n
for a, b in edges:
    parent[new[b]] = max(parent[new[b]], new[a])

for i in range(n):
    if parent[new[i]] == -1:
        print(0)
    else:
        print(topo[parent[new[i]]] + 1)
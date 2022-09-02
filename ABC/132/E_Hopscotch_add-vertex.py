import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict, deque

def bfs(u, mod):
    dist[u][mod] = 0
    q = deque()
    q.append((u, mod))
    while q:
        v, mod = q.popleft()
        for nv, nmod in g[(v, mod)]:
            if dist[nv][nmod] != -1:
                continue
            dist[nv][nmod] = dist[v][mod] + 1
            q.append((nv, nmod))


n, m = map(int, input().split())

g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[(a, 0)].append((b, 1))
    g[(a, 1)].append((b, 2))
    g[(a, 2)].append((b, 0))

S, T = map(lambda x: int(x) - 1, input().split())

dist = [[-1] * 3 for _ in range(n)]
bfs(S, 0)
print(dist[T][0] // 3)
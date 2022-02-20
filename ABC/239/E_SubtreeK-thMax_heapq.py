from collections import defaultdict
from heapq import heappush, heappushpop, nlargest
import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)

        for m in num[nv]:
            if len(num[v]) > 20:
                heappushpop(num[v], m)
            else:
                heappush(num[v], m)


n, q = map(int, input().split())
X = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

num = [[] for _ in range(n)]
for i, x in enumerate(X):
    heappush(num[i], x)

dfs(0, -1)

for _ in range(q):
    v, k = map(int, input().split())
    v -= 1
    print(nlargest(k, num[v])[-1])
import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v):
    global num_v, edge
    seen[v] = 1
    num_v += 1
    edge += len(g[v])
    for nv in g[v]:
        if seen[nv]:
            continue
        dfs(nv)


n, m = map(int, input().split())
MOD = 998244353

g = defaultdict(list)
for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

seen = [0] * n
group = 0
for i in range(n):
    if seen[i]:
        continue
    num_v = 0
    edge = 0
    dfs(i)
    if edge // 2 != num_v:
        print(0)
        exit()
    group += 1

print(pow(2, group, MOD))
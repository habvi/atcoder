from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        count_[nv] += count_[v]
        dfs(nv, v)


n, Q = map(int, input().split())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

count_ = [0] * n
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    count_[p] += x

dfs(0, -1)
print(*count_)
import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs1(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        dfs1(nv, v)

    sub[v] = 1
    for nv in g[v]:
        if nv == p:
            continue
        sub[v] += sub[nv]


def dfs2(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        ans[nv] = ans[v] + (n - sub[nv]) - sub[nv]
        dfs2(nv, v)


n = int(input())

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

sub = [0] * n
dfs1(0, -1)

ans = [0] * n
ans[0] = sum(sub) - n
dfs2(0, -1)

print(*ans)
import sys
sys.setrecursionlimit(10 ** 7)
from bisect import bisect, bisect_left
from collections import defaultdict

def dfs(v, p, d):
    global num
    in_[v] = num
    dist[d].append(num)
    num += 1

    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v, d + 1)

    out_[v] = num
    dist[d].append(num)
    num += 1


n = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))

g = defaultdict(list)
for i, p in enumerate(P, 1):
    g[p].append(i)

dist = defaultdict(list)
in_ = [None] * n
out_ = [None] * n
num = 0
dfs(0, -1, 0)

for _, v in dist.items():
    v.sort()


Q = int(input())
for _ in range(Q):
    u, d = map(int, input().split())
    u -= 1
    mn = in_[u]
    mx = out_[u]

    left = bisect_left(dist[d], mn)
    right = bisect(dist[d], mx)
    print((right - left) // 2)
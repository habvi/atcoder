import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def print_ans(v):
    i = route.index(v)
    print(len(route) - i)
    print(*map(lambda x: x + 1, route[i:]))
    exit()

def dfs(v):
    for nv in g[v]:
        if seen[nv]:
            print_ans(nv)
        route.append(nv)
        seen[nv] = 1
        dfs(nv)


N = int(input())
A = list(map(int, input().split()))

g = defaultdict(list)
for i, a in enumerate(A):
    a -= 1
    g[i].append(a)

seen = [0] * N
for v in range(N):
    if seen[v]:
        continue
    seen[v] = 1
    route = [v]
    dfs(v)
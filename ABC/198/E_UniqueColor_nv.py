import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        nc = C[nv]
        if used[nc] == 0:
            ans.append(nv + 1)
        used[nc] += 1
        dfs(nv, v)
        used[nc] -= 1


N = int(input())
C = list(map(int, input().split()))

g = defaultdict(list)
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

used = defaultdict(int)
used[C[0]] = 1
ans = [1]
dfs(0, -1)
print(*sorted(ans))
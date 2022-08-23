from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p):
    c = C[v]
    if used[c] == 0:
        ans.append(v + 1)
    used[c] += 1
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
    used[c] -= 1


N = int(input())
C = list(map(int, input().split()))

g = defaultdict(list)
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

ans = []
used = defaultdict(int)
dfs(0, -1)
print(*sorted(ans))
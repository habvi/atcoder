from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p):
    if cnt[c[v]] == 0:
        ans.append(v + 1)
    cnt[c[v]] += 1
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
        cnt[c[nv]] -= 1
        
n = int(input())
c = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

ans = []
cnt = defaultdict(int)
dfs(0, -1)
print(*sorted(ans))
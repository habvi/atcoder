from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v):
    if v not in d:
        return 1
    mx, mn = 0, float('inf')
    for nv in d[v]:
        mx = max(mx, dfs(nv))
        mn = min(mn, dfs(nv))
    return mx + mn + 1

n = int(input())
d = defaultdict(list)
for i in range(2, n + 1):
    a = int(input())
    d[a].append(i)
print(dfs(1))
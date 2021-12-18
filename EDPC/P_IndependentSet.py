import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p):
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
        dp[v][0] *= dp[nv][0] + dp[nv][1]
        dp[v][0] %= MOD
        dp[v][1] *= dp[nv][0]
        dp[v][1] %= MOD

from collections import defaultdict
n = int(input())
MOD = 10**9 + 7
g = defaultdict(list)
for _ in range(n - 1):
    x, y = map(lambda x: int(x) - 1, input().split())
    g[x].append(y)
    g[y].append(x)

dp = [[1] * 2 for _ in range(n)]
dfs(0, -1)
print(sum(dp[0]) % MOD)
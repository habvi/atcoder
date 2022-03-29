# PyPy only

import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p):
    if v == nxt:
        return True

    for nv, ni in g[v]:
        if nv == p:
            continue
        if dfs(nv, v):
            edge[ni] += 1
            return True
    return False


n, m, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
MOD = 998244353

g = defaultdict(list)
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append((b, i))
    g[b].append((a, i))

edge = [0] * (n - 1)
for i in range(m - 1):
    pre, nxt = A[i], A[i + 1]
    dfs(pre, -1)

total = sum(edge)
kt = K + total
if (total < K) or (kt % 2) or (kt < 0):
    print(0)
    exit()

R = kt // 2

dp = [0] * (R + 1)
dp[0] = 1
for num in edge:
    for i in reversed(range(R + 1)):
        if i + num <= R:
            dp[i + num] += dp[i]
            dp[i + num] %= MOD

print(dp[R])
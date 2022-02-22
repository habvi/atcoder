# PyPy only

from collections import defaultdict
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p):
    if v == r:
        return True
    for nv, ni in g[v]:
        if nv == p:
            continue
        if dfs(nv, v):
            seen[ni] += 1
            return True
    return False


n, m, K = map(int, input().split())
M = list(map(lambda x: int(x) - 1, input().split()))
MOD = 998244353

g = defaultdict(list)
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append((b, i))
    g[b].append((a, i))

seen = [0] * (n - 1)
for i in range(m - 1):
    l, r = M[i], M[i + 1]
    dfs(l, -1)

sm = sum(seen)
ksm = K + sm
if ksm % 2 or ksm < 0 or ksm > sm * 2:
    print(0)
    exit()

total = ksm // 2

dp = [0] * (total + 1)
dp[0] = 1

for num in seen:
    for i in reversed(range(total + 1)):
        if i + num <= total:
            dp[i + num] += dp[i]
            dp[i + num] %= MOD

print(dp[total])
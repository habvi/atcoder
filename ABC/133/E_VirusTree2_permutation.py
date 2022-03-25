# permutation ver.

import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def dfs(v, p):
    global ans
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)

    color = (K if p == -1 else K - 2)
    num = (len(g[v]) + 1 if p == -1 else len(g[v]) - 1)
    ans *= perm(color, num, MOD)
    ans %= MOD


def perm(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    return fact[n] * invfact[n - r] % MOD


n, K = map(int, input().split())
MOD = 10**9 + 7

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

lenc = 10**5 + 5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

ans = 1
dfs(0, -1)

print(ans)
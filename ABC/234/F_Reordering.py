from collections import Counter
def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD

s = input()
n = len(s)
MOD = 998244353

lenc = n + 5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

c = Counter(s)
dp = [0] * (n + 1)
dp[0] = 1
for _, v in c.items():
    ndp = [0] * (n + 1)
    for k in range(v + 1):
        for i in range(n - k + 1):
            j = i + k
            ndp[j] += dp[i] * comb(j, i, MOD)
            ndp[j] %= MOD
    dp = ndp

ans = 0
for i in range(1, n + 1):
    ans += dp[i]
    ans %= MOD
print(ans)
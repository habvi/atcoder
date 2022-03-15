def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD


n, m, K = map(int, input().split())
MOD = 998244353

lenc = n + 5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

ans = 0
for i in range(K + 1):
    total = m * comb(n - 1, i, MOD) % MOD
    total *= pow(m - 1, n - i - 1, MOD)
    total %= MOD

    ans += total
    ans %= MOD

print(ans)
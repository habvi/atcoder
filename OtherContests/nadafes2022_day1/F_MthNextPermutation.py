def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD


n, m, K = map(int, input().split())
MOD = 998244353

lenc = 2 * 10**5 + 5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD


if K == 1:
    ans = 0
    for i in range(1, n + 1):
        if m % i:
            continue
        total = comb(n - 1, i - 1, MOD)
        total *= fact[i - 1]
        total *= fact[n - i]
        total %= MOD
        ans += total
else:
    ans = 0
    for i in range(2, n + 1):
        if m % i == 0:
            continue
        total = comb(n - 2, i - 2, MOD)
        total *= fact[i - 2]
        total *= fact[n - i]
        total %= MOD
        ans += total
print(ans % MOD)
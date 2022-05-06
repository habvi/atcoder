def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD


n, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

lenc = n + 5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

A.sort()
ans = 0
for i, a in enumerate(A):
    if i >= K - 1:
        ans += a * comb(i, K - 1, MOD)
    if i <= n - K:
        ans -= a * comb(n - i - 1, K - 1, MOD)
print((ans + MOD) % MOD)
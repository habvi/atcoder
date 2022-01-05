def comb(n, k, MOD):
    nmrt = fact[n]
    dnmnt = invfact[n - k] * invfact[k] % MOD
    return nmrt * dnmnt % MOD

w, h = map(int, input().split())
MOD = 10**9 + 7

lenc = w + h
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

print(comb(w + h - 2, min(w, h) - 1, MOD))
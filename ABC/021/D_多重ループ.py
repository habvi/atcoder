def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD

def nHr(n, r):
    return comb(n + r - 1, r, MOD)

MOD = 10**9 + 7
lenc = 2 * 10**5 + 10
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

n = int(input())
k = int(input())
print(nHr(n, k))
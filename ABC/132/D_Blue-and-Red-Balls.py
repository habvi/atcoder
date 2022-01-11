def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD

n, k = map(int, input().split())
B = k
R = n - k
MOD = 10**9 + 7

lenc = 2010
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

for i in range(k):
    if i == 0:
        print(n - k + 1)
        continue
    
    ans = comb(B - 1, i, MOD)
    
    r = comb(R - 1, i - 1, MOD)
    r += comb(R - 1, i, MOD) * 2
    r += comb(R - 1, i + 1, MOD)
    print(ans * r % MOD)
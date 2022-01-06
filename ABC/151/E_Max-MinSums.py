def comb(n, k, MOD):
    nmrt = fact[n]
    dnmnt = invfact[n - k] * invfact[k] % MOD
    return nmrt * dnmnt % MOD

MOD = 10**9 + 7
lenc = 10**5 + 5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD
    
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(n):
    if i >= k - 1:
        ans += a[i] * comb(i, k - 1, MOD)
        ans -= a[-i-1] * comb(i, k - 1, MOD)
print(ans % MOD)
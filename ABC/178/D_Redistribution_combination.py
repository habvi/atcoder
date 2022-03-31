def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD


n = int(input())
MOD = 10**9 + 7

lenc = 2 * n + 5
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD


ans = 0
for box in range(1, n // 3 + 1):
    res = n - 3 * box
    if res < 0:
        break

    ans += comb(box - 1 + res, res, MOD)
    ans %= MOD
print(ans)
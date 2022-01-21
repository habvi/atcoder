n, a, b = map(int, input().split())
MOD = 10**9 + 7

lenc = 2 * 10**5 + 5
invfact = [1] * (lenc)
for i in range(2, lenc):
    invfact[i] = invfact[MOD % i] * (MOD - MOD // i) % MOD

def comb(n, k, MOD):
    if n < k or n < 0 or k < 0:
        return 0
    x = 1
    for i in range(k):
        x *= (n-i)
        x *= invfact[i+1]
        x %= MOD
    return x

ans = pow(2, n, MOD) - 1
ans -= comb(n, a, MOD)
ans -= comb(n, b, MOD)
print((ans + MOD) % MOD)
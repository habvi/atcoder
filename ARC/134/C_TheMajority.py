def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    x = 1
    for i in range(r):
        x *= (n - i)
        x *= invfact[i + 1]
        x %= MOD
    return x

def nHr(n, r):
    return comb(n + r - 1, r - 1, MOD)


n, k = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353

one = A[0]
other = sum(A[1:])
if one < k or one - k < other:
    print(0)
    exit()

one -= k + other

lenc = k + 1
invfact = [1] * (lenc)
for i in range(2, lenc):
    invfact[i] = invfact[MOD % i] * (MOD - MOD // i) % MOD
    
ans = nHr(one, k)
for a in A[1:]:
    ans *= nHr(a, k)
    ans %= MOD
print(ans)
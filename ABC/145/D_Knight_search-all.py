def comb_mod(n, r, MOD):
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % MOD
        denom = denom * i % MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD


X, Y = map(int, input().split())
MOD = 10**9 + 7

# a + 2*b = X
# 2*a + b = Y
for a in range(X + 1):
    b = Y - 2*a
    if b < 0:
        continue
    if (a + 2*b) == X:
        print(comb_mod(a + b, a, MOD))
        exit()
print(0)
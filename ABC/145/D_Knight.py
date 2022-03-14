def comb_mod(n, r, mod):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


x, y = map(int, input().split())
MOD = 10**9 + 7

if (x + y) % 3:
    print(0)
    exit()

b = (-x + 2*y) // 3
a = y - 2*b

if a >= 0 and b >= 0:
    print(comb_mod(a + b, a, MOD))
else:
    print(0)
def comb_mod(n, r, MOD):
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % MOD
        denom = denom * i % MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD


n, K = map(int, input().split())
MOD = 998244353

mid = n // 2

if K < n - mid:
    print(0)
    exit()

ans = comb_mod(mid, K - n + mid, MOD)
print(ans)
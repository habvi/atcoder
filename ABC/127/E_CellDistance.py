def calc_dist(h, w):
    dist = 0
    for dy in range(1, h + 1):
        times = h - dy
        dist += w * w * dy * times
    return dist

def comb_mod(n, r, MOD):
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % MOD
        denom = denom * i % MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD


n, m, K = map(int, input().split())
MOD = 10**9 + 7

total = calc_dist(n, m) + calc_dist(m, n)
num = comb_mod(n * m - 2, K - 2, MOD)
print(total * num % MOD)
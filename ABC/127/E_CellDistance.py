def solve(h, w):
    global total
    dist = 0
    for dx in range(w):
        num = w - dx
        dist += h * h * dx * num
    total += dist

def comb_mod(n, r, MOD):
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % MOD
        denom = denom * i % MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD


n, m, K = map(int, input().split())
MOD = 10**9 + 7

total = 0
solve(n, m)
solve(m, n)
times = comb_mod(n * m - 2, K - 2, MOD)
print(total * times % MOD)
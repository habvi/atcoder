n, a, b = map(int, input().split())
MOD = 10**9 + 7

len_inv = 2*(10**5) + 10
inv = [1]*(len_inv)
for i in range(2, len_inv):
    inv[i] = inv[MOD%i] * (MOD - MOD//i) % MOD

def comb(n, k, MOD):
    x = 1
    for i in range(k):
        x *= (n-i)
        x *= inv[i+1]
        x %= MOD
    return x

ans = pow(2, n, MOD) - 1
ans -= comb(n, a, MOD)
ans -= comb(n, b, MOD)
print((ans + MOD) % MOD)
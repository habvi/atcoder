n, k, m = map(int, input().split())
MOD = 998244353

x = pow(k, n, MOD - 1)
if m % MOD == 0:
    print(0)
else:
    print(pow(m, x, MOD))
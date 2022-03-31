n = int(input())
MOD = 10**9 + 7

p10 = pow(10, n, MOD)
p9 = pow(9, n, MOD)
p8 = pow(8, n, MOD)

ans = p10 - p9 + p10 - p9 - (p10 - p8)
print((ans + MOD) % MOD)
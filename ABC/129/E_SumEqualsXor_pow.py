L = input()
n = len(L)
MOD = 10**9 + 7

ans = 0
one = 0
for i, bit in enumerate(L):
    if bit == '1':
        ans += pow(2, one, MOD) * pow(3, n - i - 1, MOD)
        ans %= MOD
        one += 1

ans += pow(2, one, MOD)
print(ans % MOD)
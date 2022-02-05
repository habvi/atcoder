def sigma(x):
    return x * (x + 1) // 2


n = int(input())
MOD = 998244353

k = len(str(n))
ans = 0
for i in range(1, k):
    ans += sigma(9 * 10**(i - 1))
    ans %= MOD

ans += sigma(n - 10**(k - 1) + 1)
ans %= MOD
print(ans)
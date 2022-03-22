n = int(input())
A = list(map(int, input().split()))
MOD = 998244353

m = 10
dp = [0] * m
A = A[::-1]
dp[A.pop()] = 1

while A:
    ndp = [0] * m

    x = A.pop()
    for y in range(m):
        ndp[(x + y) % 10] += dp[y]
        ndp[(x + y) % 10] %= MOD
        ndp[(x * y) % 10] += dp[y]
        ndp[(x * y) % 10] %= MOD

    dp = ndp
print(*dp)
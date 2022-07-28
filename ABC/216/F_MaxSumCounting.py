N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

ab = []
for a, b in zip(A, B):
    ab.append((a, b))
ab.sort()

mx = max(A)
dp = [0] * (mx + 1)
dp[0] = 1
ans = 0
for a, b in ab:
    ndp = [0] * (mx + 1)
    for i in range(mx + 1):
        ndp[i] = dp[i]
        if i - b >= 0:
            ndp[i] += dp[i - b]
            ndp[i] %= MOD
        if i <= a - b:
            ans += dp[i]
            ans %= MOD
    dp = ndp
print(ans)

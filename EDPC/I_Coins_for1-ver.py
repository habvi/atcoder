n = int(input())
P = tuple(map(float, input().split()))

dp = [0] * (n + 1)
dp[0] = 1

for p in P:
    ndp = [0] * (n + 1)
    for i in range(n):
        ndp[i] += dp[i] * (1 - p)
        ndp[i + 1] += dp[i] * p
    dp = ndp

ans = 0
for i in range((n + 1)//2, n + 1):
    ans += dp[i]
print(ans)
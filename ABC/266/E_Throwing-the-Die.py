N = int(input())

dp = list(range(1, 7))
ans = 0
for _ in range(N):
    mx = 0
    for i in range(6):
        mx += (1 / 6) * dp[i]
    ans = max(ans, mx)
    for i in range(6):
        dp[i] = max(dp[i], mx)
print(ans)
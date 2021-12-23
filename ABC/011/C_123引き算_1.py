n = int(input())
ng = [int(input()) for _ in range(3)]
mx = 300
INF = 500
dp = [INF] * (mx + 1)
dp[0] = 0
for i in ng:
    dp[i] = -1

for i in range(1, mx + 1):
    if i - 1 >= 0 and 0 <= dp[i - 1] < 100 and dp[i] != -1:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    if i - 2 >= 0 and 0 <= dp[i - 2] < 100 and dp[i] != -1:
        dp[i] = min(dp[i], dp[i - 2] + 1)
    if i - 3 >= 0 and 0 <= dp[i - 3] < 100 and dp[i] != -1:
        dp[i] = min(dp[i], dp[i - 3] + 1)
print('NO' if dp[n] in (-1, INF) else 'YES')
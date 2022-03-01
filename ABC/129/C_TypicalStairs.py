n, m = map(int, input().split())
MOD = 10**9 + 7

dp = [0] * (n + 1)
dp[0] = 1
for _ in range(m):
    a = int(input())
    dp[a] = -1

for i in range(1, n + 1):
    if dp[i] == -1:
        continue

    if dp[i - 1] != -1:
        dp[i] += dp[i - 1]

    if i - 2 >= 0 and dp[i - 2] != -1:
        dp[i] += dp[i - 2]

    dp[i] %= MOD

print(dp[n])
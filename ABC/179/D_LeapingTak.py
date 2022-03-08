n, k = map(int, input().split())
lr = [tuple(map(int, input().split())) for _ in range(k)]
MOD = 998244353

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    total = 0
    for L, R in lr:
        R += 1
        l = max(0, i - R)
        r = max(0, i - L)
        total += dp[r] - dp[l]

    dp[i] = dp[i - 1] + total
    dp[i] %= MOD
 
print((dp[-1] - dp[-2] + MOD) % MOD)



# 配るDP
# n, k = map(int, input().split())
# lr = [list(map(int, input().split())) for _ in range(k)]
# MOD = 998244353

# dp = [0] * (n + 1)
# dp[0] = 1

# for i in range(n):
#     for L, R in lr:
#         R += 1
#         l = min(i + L, n)
#         r = min(i + R, n)
#         dp[l] += dp[i]
#         dp[r] -= dp[i]

#     if i >= 1:
#         dp[i + 1] += dp[i]
#         dp[i + 1] %= MOD

# print(dp[n - 1])
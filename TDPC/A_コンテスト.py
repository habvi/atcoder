n = int(input())
P = list(map(int, input().split()))
m = sum(P)
dp = [0] * (m + 1)
dp[0] = 1
for p in P:
    for i in range(m - p, -1, -1):
        dp[i + p] |= dp[i]
print(sum(dp))
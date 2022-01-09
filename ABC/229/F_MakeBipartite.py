# 解説後
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = [b[-1]] + b[:-1]

ans = float('inf')
for si in range(2):
    dp = [float('inf')] * 2
    dp[si] = 0
    for i in range(n):
        ndp = [float('inf')] * 2
        dp, ndp = ndp, dp
        for pj in range(2):
            for j in range(2):
                now = ndp[pj]
                if j == 0:
                    now += a[i]
                if j == pj:
                    now += b[i]
                dp[j] = min(dp[j], now)
    ans = min(ans, dp[si])
print(ans)
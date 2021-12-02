h, n = map(int, input().split())
dp = [float('inf')] * (h + 1)
dp[0] = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(h + 1):
        dp[min(i + a, h)] = min(dp[min(i + a, h)], dp[i] + b)  
print(dp[h])
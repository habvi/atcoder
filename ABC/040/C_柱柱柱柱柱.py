n = int(input())
A = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * n
dp[0] = 0
for i in range(n):
    if i - 1 >= 0:
        dp[i] = min(dp[i], dp[i - 1] + abs(A[i] - A[i - 1]))
    if i - 2 >= 0:
        dp[i] = min(dp[i], dp[i - 2] + abs(A[i] - A[i - 2]))

print(dp[-1])
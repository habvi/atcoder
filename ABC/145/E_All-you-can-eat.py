n, T = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort()

t = T + 3000
INF = float('inf')
dp = [-INF] * (t + 1)
dp[0] = 0
for a, b in ab:
    for i in reversed(range(T)):
        dp[i + a] = max(dp[i + a], dp[i] + b)

print(max(dp))
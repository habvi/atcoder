n, W = map(int, input().split())

INF = float('inf')
mx = n * 10**3
dp = [INF] * (mx + 1)
dp[0] = 0

for _ in range(n):
    w, v = map(int, input().split())

    for i in reversed(range(mx + 1)):
        if i - v >= 0:
            dp[i] = min(dp[i], dp[i - v] + w)

for i in reversed(range(mx + 1)):
    if dp[i] <= W:
        print(i)
        exit()
n = int(input())

cand = [1]
for i in (6, 9):
    cand.append(i)
    while cand[-1] * i <= n:
        cand.append(cand[-1] * i)

INF = float('inf')
dp = [INF] * (n + 1)
dp[0] = 0
for x in cand:
    for i in range(n + 1):
        if i + x <= n:
            dp[i + x] = min(dp[i + x], dp[i] + 1)

print(dp[n])
def update(i, dist, cost):
    if i + dist <= L:
        if i + dist in X:
            cost += T3
        dp[i + dist] = min(dp[i + dist], dp[i] + cost)


n, L = map(int, input().split())
X = set(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

INF = float('inf')
dp = [INF] * (L + 1)
dp[0] = 0

for i in range(L):
    update(i, 1, T1)
    update(i, 2, T1 + T2)
    update(i, 4, T1 + T2 * 3)
    if i + 4 > L:
        cost = T1 // 2 + T2 * ((L - i - 1) * 2 + 1) // 2
        dp[L] = min(dp[L], dp[i] + cost)

print(dp[-1])
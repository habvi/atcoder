n, X = map(int, input().split())
A = list(map(int, input().split()))

INF = float('inf')
ans = INF
for k in range(1, n + 1):
    # mod, kind
    dp = [[-INF] * k for _ in range(k + 1)]
    dp[0][0] = 0

    for a in A:
        for kind in reversed(range(k)):
            for mod in range(k):
                if dp[kind][mod] == -INF:
                    continue
                total = dp[kind][mod] + a
                nxt = (X - total) % k
                dp[kind + 1][nxt] = max(dp[kind + 1][nxt], total)

    ans = min(ans, (X - dp[k][0]) // k)
print(ans)
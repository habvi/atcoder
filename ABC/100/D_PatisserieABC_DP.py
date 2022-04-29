n, m = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(n)]

INF = float('inf')
ans = -INF
for bit in range(1 << 3):
    dp = [-INF] * (m + 1)
    dp[0] = 0
    for x, y, z in xyz:
        total = 0
        for i, v in enumerate((x, y, z)):
            if bit >> i & 1:
                total += v
            else:
                total += -v

        for i in reversed(range(1, m + 1)):
            dp[i] = max(dp[i], dp[i - 1] + total)

    ans = max(ans, dp[-1])
print(ans)
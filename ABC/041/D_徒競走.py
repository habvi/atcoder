n, m = map(int, input().split())

include = [0] * n
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    include[x] |= (1 << y)

dp = [0] * (1 << n)
dp[0] = 1
for now in range(1 << n):
    for v in range(n):
        if now & 1 << v:
            continue
        if include[v] & now:
            continue
        nxt = now | 1 << v
        dp[nxt] += dp[now]

print(dp[-1])
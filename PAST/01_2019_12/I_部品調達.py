n, m = map(int, input().split())
sc = []
for _ in range(m):
    s, c = input().split()
    s = ['1' if yn == 'Y' else '0' for yn in s]
    c = int(c)
    sc.append((int(''.join(s), 2), c))

INF = float('inf')
dp = [INF] * (1 << n)
dp[0] = 0
for now in range(1 << n):
    for s, c in sc:
        nxt = now | s
        dp[nxt] = min(dp[nxt], dp[now] + c)

ans = dp[-1]
print(ans if ans != INF else -1)
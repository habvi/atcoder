N, M, K = map(int, input().split())
ab = []
for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    ab.append((a, b, c))
E = list(map(lambda x: int(x) - 1, input().split()))

INF = float('inf')
dp = [INF] * N
dp[0] = 0
for e in E:
    v, nv, c = ab[e]
    dp[nv] = min(dp[nv], dp[v] + c)
ans = dp[-1]
print(ans if ans != INF else -1)
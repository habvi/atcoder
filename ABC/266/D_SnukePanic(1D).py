from collections import defaultdict

N = int(input())
mx = 10 ** 5
times = defaultdict(lambda : (0, 0))
for _ in range(N):
    T, X, A = map(int, input().split())
    times[T] = (X, A)

INF = float('inf')
dp = [-INF] * 5
dp[0] = 0
for t in range(1, mx + 1):
    ndp = [-INF] * 5
    x, a = times[t]
    for i in range(5):
        plus = (a if i == x else 0)
        if 0 <= i - 1:
            ndp[i] = max(ndp[i], dp[i - 1] + plus)
        ndp[i] = max(ndp[i], dp[i] + plus)
        if i + 1 < 5:
            ndp[i] = max(ndp[i], dp[i + 1] + plus)
    dp = ndp
print(max(dp))

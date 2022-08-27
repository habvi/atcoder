N = int(input())
mx = 10 ** 5
hole = {}
for _ in range(N):
    T, X, A = map(int, input().split())
    hole[T] = (X, A)

INF = float('inf')
dp = [-INF] * 5
dp[0] = 0
for t in range(1, mx + 1):
    ndp = [-INF] * 5
    exist = 0
    if t in hole:
        x, a = hole[t]
        exist = 1
    for i in range(5):
        plus = a if exist and i == x else 0
        ndp[i] = max(ndp[i], dp[i] + plus)
        if i - 1 >= 0:
            ndp[i] = max(ndp[i], dp[i - 1] + plus)
        if i + 1 < 5:
            ndp[i] = max(ndp[i], dp[i + 1] + plus)
    dp = ndp
print(max(dp))

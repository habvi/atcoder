from math import gcd

n, ma, mb = map(int, input().split())

m = n * 10
INF = float('inf')
dp = [[INF] * (m + 1) for _ in range(m + 1)]
dp[0][0] = 0

for _ in range(n):
    a, b, c = map(int, input().split())

    for i in reversed(range(m + 1)):
        for j in reversed(range(m + 1)):
            ni, nj = i + a, j + b
            if ni <= m and nj <= m:
                dp[ni][nj] = min(dp[ni][nj], dp[i][j] + c)

ans = INF
for i in range(1, m + 1):
    for j in range(1, m + 1):
        g = gcd(i, j)
        ni = i // g
        nj = j // g
        if (ni, nj) == (ma, mb):
            ans = min(ans, dp[i][j])

print(ans if ans != INF else -1)
from math import gcd

n, ma, mb = map(int, input().split())

mx = n * 10
INF = float('inf')
dp = [[INF] * (mx + 1) for _ in range(mx + 1)]
dp[0][0] = 0

for _ in range(n):
    a, b, c = map(int, input().split())

    for i in reversed(range(mx + 1)):
        for j in reversed(range(mx + 1)):
            ni, nj = i + a, j + b
            if ni <= mx and nj <= mx:
                dp[ni][nj] = min(dp[ni][nj], dp[i][j] + c)

ans = INF
for i in range(1, mx + 1):
    for j in range(1, mx + 1):
        g = gcd(i, j)
        ni = i // g
        nj = j // g
        if (ni, nj) == (ma, mb):
            ans = min(ans, dp[i][j])

print(ans if ans != INF else -1)
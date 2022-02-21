from collections import Counter

n = int(input())
A = list(map(int, input().split()))

m = 302
dp = [[[0] * m for _ in range(m)] for _ in range(m)]

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            total = i + j + k
            if total == 0:
                continue

            dp[i][j][k] = n / total

            if i - 1 >= 0:
                dp[i][j][k] += dp[i - 1][j + 1][k] * (i / total)
            if j - 1 >= 0:
                dp[i][j][k] += dp[i][j - 1][k + 1] * (j / total)
            if k - 1 >= 0:
                dp[i][j][k] += dp[i][j][k - 1] * (k / total)

c = Counter(A)
print(dp[c[3]][c[2]][c[1]])
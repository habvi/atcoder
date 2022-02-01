n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(3)]
for i in range(3):
    dp[i][0] = A[0][i]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[j][i] = max(dp[j][i], dp[k][i - 1] + A[i][j])
            
print(max(dp[i][-1] for i in range(3)))
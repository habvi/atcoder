n, K = map(int, input().split())
MOD = 10000

decided = [-1] * n
for _ in range(K):
    a, b = map(int, input().split())
    decided[a - 1] = b - 1

# today; yesterday
dp = [[0] * 3 for _ in range(3)]
y, t = decided[0], decided[1]
if y >= 0 and t >= 0:
    dp[y][t] = 1
elif y >= 0:
    for i in range(3):
        dp[y][i] = 1
elif t >= 0:
    for i in range(3):
        dp[i][t] = 1
else:
    dp = [[1] * 3 for _ in range(3)]

for day in range(2, n):
    ndp = [[0] * 3 for _ in range(3)]
    if decided[day] >= 0:
        for i in range(3):
            j = decided[day]
            for y in range(3):
                for t in range(3):
                    if t != i or y == t == j:
                        continue
                    ndp[i][j] += dp[y][t]
                    ndp[i][j] %= MOD
    else:
        for i in range(3):
            for j in range(3):
                for y in range(3):
                    for t in range(3):
                        if t != i or y == t == j:
                            continue
                        ndp[i][j] += dp[y][t]
                        ndp[i][j] %= MOD
    dp = ndp
print(sum(sum(ans) for ans in dp) % MOD)
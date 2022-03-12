h, w = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(h)]
B = [tuple(map(int, input().split())) for _ in range(h)]

dif = [[None] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        dif[i][j] = abs(A[i][j] - B[i][j])

BU = 80 * (h + w)

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1 << (BU - dif[0][0]) | 1 << (BU + dif[0][0])

for i in range(h):
    for j in range(w):
        if i > 0:
            dp[i][j] |= dp[i - 1][j] << dif[i][j]
            dp[i][j] |= dp[i - 1][j] >> dif[i][j]
        if j > 0:
            dp[i][j] |= dp[i][j - 1] << dif[i][j]
            dp[i][j] |= dp[i][j - 1] >> dif[i][j]

ans = float('inf')
num = dp[-1][-1]
for i in range(BU * 2):
    if num >> i & 1:
        ans = min(ans, abs(i - BU))
print(ans)
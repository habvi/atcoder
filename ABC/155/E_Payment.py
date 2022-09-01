S = '0' + input()

INF = float('inf')
# just, + 1
dp = [INF] * 2
dp[0] = 0
for x in S[::-1]:
    ndp = [INF] * 2
    for i in range(2):
        x = int(x) + i
        if x < 10:
            ndp[0] = min(ndp[0], dp[i] + x)
        if x > 0:
            ndp[1] = min(ndp[1], dp[i] + (10 - x))
    dp = ndp
print(dp[0])



# -------------------
S = input()

INF = float('inf')
# just, + 1
dp = [INF] * 2
dp[0] = 0
for x in S[::-1]:
    ndp = [INF] * 2
    for i in range(2):
        x = int(x) + i
        if x < 10:
            ndp[0] = min(ndp[0], dp[i] + x)
        if x > 0:
            ndp[1] = min(ndp[1], dp[i] + (10 - x))
    dp = ndp
print(min(dp[0], dp[1] + 1))

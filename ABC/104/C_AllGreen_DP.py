D, G = map(int, input().split())
pc = [tuple(map(int, input().split())) for _ in range(D)]

n = 1001
dp = [0] * n
for i, (q, bonus) in enumerate(pc, 1):
    ndp = [0] * n

    for j in range(n):
        for num in range(q):
            if j + num < n:
                ndp[j + num] = max(ndp[j + num], dp[j] + i * 100 * num)
        if j + q < n:
            ndp[j + q] = max(ndp[j + q], dp[j] + i * 100 * q + bonus)

    dp = ndp

for i, point in enumerate(dp):
    if point >= G:
        print(i)
        exit()
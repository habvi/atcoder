D, G = map(int, input().split())
pc = [tuple(map(int, input().split())) for _ in range(D)]

mx = 100 * 10
dp = [0] * (mx + 1)
for i, (q, bonus) in enumerate(pc, 1):
    ndp = [0] * (mx + 1)
    for j in range(mx + 1):
        for num in range(q):
            if j + num <= mx:
                ndp[j + num] = max(ndp[j + num], dp[j] + 100*i*num)
        if j + q <= mx:
            ndp[j + q] = max(ndp[j + q], dp[j] + 100*i*q + bonus)
    dp = ndp

for i, score in enumerate(dp):
    if score >= G:
        print(i)
        exit()
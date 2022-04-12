def update(now):
    for pre, num in enumerate(dp):
        nxt = (now * k + pre) % m
        ndp[nxt] += num
        ndp[nxt] %= MOD


S = input()
MOD = 10**9 + 7

m = 13
dp = [0] * m
dp[0] = 1
k = 1
for s in S[::-1]:
    ndp = [0] * m
    if s == '?':
        for now in range(10):
            update(now)
    else:
        now = int(s)
        update(now)

    k *= 10
    k %= m
    dp = ndp

print(dp[5])
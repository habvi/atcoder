def update(num):
    for pre, num in enumerate(dp):
        nxt = (pre + num * power) % m
        ndp[nxt] += num
        ndp[nxt] %= MOD


S = input()
MOD = 10**9 + 7

m = 13
dp = [0] * m
dp[0] = 1
power = 1
for s in S[::-1]:
    ndp = [0] * m
    if s == '?':
        for num in range(10):
            update(num)
    else:
        num = int(s)
        update(num)
    power *= 10
    power %= m
    dp = ndp
print(dp[5])
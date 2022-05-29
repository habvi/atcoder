n, m = map(int, input().split())
MOD = 998244353

bit = m.bit_length()
if n > bit:
    print(0)
    exit()

num = [0] * (bit + 1)
num[1] = 1
for i in range(2, bit + 1):
    num[i] = num[i - 1] * 2 % MOD
    if i == bit:
        num[i] = (m - num[i] + 1) % MOD

dp = num[:]
for _ in range(n - 1):
    ndp = [0] * (bit + 1)
    for pre in range(1, bit + 1):
        for now in range(pre + 1, bit + 1):
            ndp[now] += dp[pre] * num[now]
            ndp[now] %= MOD
    dp = ndp

print(sum(dp) % MOD)
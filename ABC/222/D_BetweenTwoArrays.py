n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 998244353

def accumulate_mod(lis, MOD):
    ac = [lis[0] % MOD]
    for x in lis[1:]:
        ac.append((ac[-1] + x) % MOD)
    return ac

dp = [0] * 3001
for i in range(a[0], b[0] + 1):
    dp[i] += 1
dp = accumulate_mod(dp, MOD)

for i in range(1, n):
    ndp = [0] * 3001
    for j in range(a[i], b[i] + 1):
        ndp[j] = dp[j]
    dp = accumulate_mod(ndp, MOD)
print(dp[b[-1]])
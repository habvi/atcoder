n = int(input())
a = list(map(int,input().split()))
MOD = 10**9 + 7

dpp = [0] * n
dpp[0] = 1
dpm = [0] * n
for i in range(n - 1):
    dpp[i + 1] += (dpp[i] + dpm[i]) % MOD
    dpm[i + 1] += dpp[i] % MOD

ans = a[0] * (dpp[-1] + dpm[-1])
for i in range(1, n):
    ans += a[i] * (dpp[i] * dpp[-i] - dpm[i] * dpm[-i])
    ans %= MOD
print(ans)
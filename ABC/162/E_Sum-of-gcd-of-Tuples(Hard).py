n, k = map(int, input().split())
MOD = 10**9 + 7
cnt = [0] * (k + 1)
for i in range(k, 0, -1):
    cnt[i] = pow(k // i, n, MOD)
    for j in range(i * 2, k + 1, i):
        cnt[i] -= cnt[j]

ans = 0
for i in range(k + 1):
    ans += cnt[i] * i
    ans %= MOD
print(ans)
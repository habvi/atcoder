N, D = map(int, input().split())
MOD = 998244353

exp = [1]
for _ in range(N):
    exp.append(exp[-1] * 2 % MOD)

ans = 0
for l in range(D + 1):
    r = D - l
    if l >= N or r >= N:
        continue
    total = exp[N - max(l, r)] - 1
    total *= exp[max(0, l - 1)]
    total *= exp[max(0, r - 1)]
    ans += (total * 2)
    ans %= MOD
print(ans)
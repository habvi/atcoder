def accumulate_mod(lis, MOD):
    ac = [lis[0] % MOD]
    for x in lis[1:]:
        ac.append((ac[-1] + x) % MOD)
    return ac


n = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

ac = accumulate_mod(A, MOD)

ans = 0
total = ac[-1]
for i, a in enumerate(A):
    ans += a * (total - ac[i])
    ans %= MOD
print(ans)
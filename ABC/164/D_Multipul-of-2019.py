from collections import Counter

def accumulate_mod(lis, MOD):
    ac = [lis[0] % MOD]
    for x in lis[1:]:
        ac.append((ac[-1] + x) % MOD)
    return ac

def nC2(x):
    return x * (x - 1) // 2


S = input()
MOD = 2019

A = []
for i, s in enumerate(S[::-1]):
    A.append(pow(10, i, MOD) * int(s) % MOD)

ac = accumulate_mod([0, *A], MOD)

ans = 0
for v in Counter(ac).values():
    if v >= 2:
        ans += nC2(v)
print(ans)
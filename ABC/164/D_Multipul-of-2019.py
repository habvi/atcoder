from collections import Counter

S = input()
MOD = 2019

power = 1
ac = [0]
for s in S[::-1]:
    num = int(s) * power % MOD
    ac.append((ac[-1] + num) % MOD)
    power *= 10
    power %= MOD

ans = 0
for v in Counter(ac).values():
    if v >= 2:
        ans += v * (v - 1) // 2
print(ans)
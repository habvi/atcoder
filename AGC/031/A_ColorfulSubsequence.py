from collections import Counter
n = int(input())
s = input()
MOD = 10**9 + 7

c = Counter(s)
ans = 1
for _, v in c.items():
    ans *= (v + 1)
    ans %= MOD
print(ans - 1)
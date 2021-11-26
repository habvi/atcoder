from collections import defaultdict
def pfact(x):
    res = []
    for i in range(2, int(x**0.5)+1):
        while x%i == 0:
            x //= i
            a[i] += 1
    if x >= 2: a[x] += 1
    return res

n = int(input())
MOD = 10 ** 9 + 7
a = defaultdict(int)
for i in range(1, n + 1):
    res = pfact(i)

ans = 1
for v in a.values():
    ans *= (v + 1)
    ans %= MOD
print(ans)
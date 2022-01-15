def pfact(x):
    res = []
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x //= i
            res.append(i)
    if x >= 2: res.append(x)
    return res

from collections import Counter
n, p = map(int, input().split())
ans = 1
for k, v in Counter(pfact(p)).items():
    if v >= n:
        ans *= pow(k, v // n)
print(ans)
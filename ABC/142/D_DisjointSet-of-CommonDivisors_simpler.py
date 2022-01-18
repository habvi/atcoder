def pfact(x):
    res = []
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x //= i
            res.append(i)
    if x >= 2: res.append(x)
    return res

from math import gcd
a, b = map(int, input().split())
p = pfact(gcd(a, b))
print(len(set(p)) + 1)
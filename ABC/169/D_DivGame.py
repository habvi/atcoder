from itertools import accumulate
from collections import Counter
from bisect import bisect

def pfact(x):
    res = []
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x //= i
            res.append(i)
    if x >= 2:
        res.append(x)
    return res


n = int(input())

ac = list(accumulate(range(1, 10)))

ans = 0
for _, v in Counter(pfact(n)).items():
    ans += bisect(ac, v)
print(ans)
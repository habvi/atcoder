from collections import defaultdict
from fractions import Fraction
from functools import cmp_to_key

def to_fraction(a, b):
    if a == b == 0:
        return (0, 0)
    if b == 0:
        return (1, 0)
    f = Fraction(a, b)
    f = (f.numerator, f.denominator)
    return f

def cmp(a, b):
    if a[0] * b[1] == b[0] * a[1]:
        return 0
    return -1 if a[0] * b[1] < b[0] * a[1] else 1


N = int(input())
d = defaultdict(list)
ab = set()
for i in range(N):
    a, b = map(int, input().split())
    f = to_fraction(a, b)
    d[f].append(i + 1)
    ab.add(f)

sorted_ab = sorted(list(ab), key=cmp_to_key(cmp))
for ab in reversed(sorted_ab):
    for i in sorted(d[ab]):
        print(i)
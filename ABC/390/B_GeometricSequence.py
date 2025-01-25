from fractions import Fraction


def to_fraction(a, b):
    if a == b == 0:
        return (0, 0)
    if b == 0:
        return (1, 0)
    f = Fraction(a, b)
    f = (f.numerator, f.denominator)
    return f


N = int(input())
A = list(map(int, input().split()))

s = set()
for i in range(N - 1):
    s.add(to_fraction(A[i], A[i + 1]))
print("Yes" if len(s) == 1 else "No")

from math import atan2, degrees, pi

a, b, x = map(int, input().split())

S = x / a
half = a * b / 2
if S <= half:
    print(degrees(pi / 2 - atan2(2 * S / b, b)))
else:
    print(degrees(atan2(2 * b - 2 * S / a, a)))
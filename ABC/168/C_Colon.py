import math
a, b, h, m = map(int, input().split())
tn = h * 360 // 12 + m * 30 / 60
ch = 360 // 60 * m
d = abs(tn - ch)
print((a**2 + b**2 - 2*a*b*math.cos(math.radians(d))) ** 0.5)
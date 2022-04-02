from math import sin, cos, atan2

x, y = map(int, input().split())

angle = atan2(y, x)
print(cos(angle), sin(angle))
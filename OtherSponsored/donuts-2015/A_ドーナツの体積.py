from math import pi

R, D = map(int, input().split())

S = R * R * pi
L = 2 * pi * D
print(S * L)
from math import cos, radians

def law_of_cos(a, b, angle):
    return (a**2 + b**2 - 2*a*b*cos(radians(angle))) ** 0.5


A, B, H, M = map(int, input().split())

long = 360 // 12 * H + 360 / 12 / 60 * M
short = 360 // 60 * M
print(law_of_cos(A, B, long - short))
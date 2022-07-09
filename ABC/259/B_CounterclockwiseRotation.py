from math import radians, degrees, sin, cos, atan2

def dist_two_points(x1, y1, x2, y2) -> float:
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def declination(x1, y1, x2, y2):
    return atan2(y2 - y1, x2 - x1)

def point(r, x, y, d):
    return x + r*cos(radians(d)), y + r*sin(radians(d))


a, b, d = map(int, input().split())

r = dist_two_points(0, 0, a, b)
print(*point(r, 0, 0, degrees(declination(0, 0, a, b)) + d))
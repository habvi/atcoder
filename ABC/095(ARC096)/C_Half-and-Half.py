a, b, c, x, y = map(int, input().split())

if x > y:
    x, y = y, x
    a, b = b, a

z = 2 * c
print(min(a*x + b*y, x*z + (y - x)*b, y*z))
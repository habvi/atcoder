from math import ceil

R, X, Y = map(int, input().split())

a = (X ** 2 + Y ** 2) ** 0.5
if a == R:
    ans = 1
elif a <= 2 * R:
    ans = 2
else:
    ans = ceil(a / R)
print(ans)
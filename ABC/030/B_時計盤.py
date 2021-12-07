n, m = map(int, input().split())
n %= 12
a = 360 // 12 * n + 360 / 12 / 60 * m
b = 360 // 60 * m
c = abs(a - b)
print(min(360 - c, c))
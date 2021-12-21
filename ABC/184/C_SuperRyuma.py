a, b = map(int, input().split())
c, d = map(int, input().split())
if (a, b) == (c, d):
    print(0)
    exit()

if a + b == c + d or a - b == c - d or abs(a - c) + abs(b - d) <= 3:
    print(1)
    exit()

if a + b - 3 <= c + d <= a + b + 3 or a - b - 3 <= c - d <= a - b + 3 or abs(a - c) + abs(b - d) <= 6 or (abs(a - c) + abs(b - d)) % 2 == 0:
    print(2)
    exit()

print(3)
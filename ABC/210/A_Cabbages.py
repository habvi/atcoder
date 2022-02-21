n, a, x, y = map(int, input().split())

print(min(a, n) * x + max(0, n - a) * y)
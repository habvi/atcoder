n, a, b = map(int, input().split())
print(min(a, b), max(0, min(a, b) - (n - max(a, b))))
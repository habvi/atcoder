a, b, c = map(int, input().split())
if a > b:
    a, b = b, a

print('Yes' if a <= c <= b else 'No')
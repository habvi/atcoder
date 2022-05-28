a, b, c = map(int, input().split())
s = sorted((a, b, c))

print('Yes' if s[1] == b else 'No')
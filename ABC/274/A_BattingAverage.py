A, B = map(int, input().split())

s = str(round(B / A, 3))
i = s.find('.')
s += '0' * (3 - len(s[i + 1:]))
print(s)
s = list(input())
a, b = map(int, input().split())
a, b = a - 1, b - 1

s[a], s[b] = s[b], s[a]
print(''.join(s))
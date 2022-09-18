a, b = input().split('.')
a = int(a)

print(a if int(b[0]) <= 4 else a + 1)
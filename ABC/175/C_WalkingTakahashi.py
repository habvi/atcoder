x, k, d = map(int, input().split())
x = abs(x)

y = x - d * k
if y >= 0:
    print(y)
    exit()

div, mod = divmod(x, d)
if k % 2 == div % 2:
    print(mod)
else:
    print(abs(mod - d))
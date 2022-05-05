n = int(input())

m = n * 2
if (x := int(m ** 0.5)) * (x + 1) >= m:
    print(x)
else:
    print(x + 1)
x = int(input())
a = int((x * 2) ** 0.5)
if a * (a + 1) >= x * 2:
    print(a)
else:
    print(a + 1)
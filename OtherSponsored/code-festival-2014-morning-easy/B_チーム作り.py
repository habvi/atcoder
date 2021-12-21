n = int(input())
if ((n - 1)//20) % 2 == 0:
    print(20 if n % 20 == 0 else n % 20)
else:
    print(1 if n % 20 == 0 else 20 - n % 20 + 1)
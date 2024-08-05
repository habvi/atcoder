Y = int(input())

if Y % 4:
    print(365)
elif Y % 100:
    print(366)
elif Y % 400:
    print(365)
else:
    print(366)

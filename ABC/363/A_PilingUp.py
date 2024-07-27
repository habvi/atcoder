R = int(input())

rates = [100, 200, 300, 400]

for rate in rates:
    if R < rate:
        print(rate - R)
        exit()

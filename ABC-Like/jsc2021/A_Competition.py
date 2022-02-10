x, y, z = map(int, input().split())

meat = y / x
for i in range(10**7, -1, -1):
    if i / z < meat:
        print(i)
        exit()
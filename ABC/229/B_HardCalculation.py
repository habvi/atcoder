a, b = input().split()
a = a[::-1]
b = b[::-1]
for x, y in zip(a, b):
    if int(x) + int(y) >= 10:
        print('Hard')
        exit()
print('Easy')
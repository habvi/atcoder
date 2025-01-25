X = int(input())

y = 1
for i in range(1, 21):
    y *= i
    if y == X:
        print(i)
        exit()

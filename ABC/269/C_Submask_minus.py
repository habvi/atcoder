N = int(input())

x = N
print(0)
while x > 0:
    x = (x - 1) & N
    print(N - x)